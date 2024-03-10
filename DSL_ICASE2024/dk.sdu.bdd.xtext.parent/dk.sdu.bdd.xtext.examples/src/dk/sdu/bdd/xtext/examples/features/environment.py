#from behave import fixture
import json
from behave.model import Scenario 

#libraries  for MT code
import time
import numpy as np
import pandas as pd
from dmp import dmp_joint


#new:
from rtde_receive import RTDEReceiveInterface as RTDEReceive
from rtde_control import RTDEControlInterface as RTDEControl
from robotiq_gripper_control import RobotiqGripper


directory_path = "C:/Users/ansil/Documents/PhD/ICASE2024/ExecutionOnRealRobot/" 
csv_path = "C:/Users/ansil/Documents/PhD/ICASE2024/robot_data_ST.csv"

f = open("Environment.json")
data = json.load(f)


#To process the csv file: return true if the row is valid
def valid(x):
    
    if(x <1439):#< 5794):
        return True
    
    return False
        
def before_all(context):
    print("Preparation of the Environment...")

    #Robot parameters
    ip = "192.168.1.12"#IP address of the UR robot
     
    #sending
    context.rtde_c = RTDEControl(ip)
    
    #reading
    frequency = 500
    context.rtde_r = RTDEReceive(ip, frequency)#(args.ip, args.frequency)
    context.output = directory_path + "/real_rob_related/realRobTrajPerform.csv" # data context.output (.csv) file to write to (default is \"robot_data.csv\""

    #context.gripper
    context.gripper = RobotiqGripper(context.rtde_c)
    print("Opening gripper...")
    context.gripper.activate()  
    context.gripper.open()

    #read dataframes
    context.df = pd.read_csv(directory_path + "NNresults.csv")
    context.results = context.df.to_numpy()

    #read ground truth 
    # read specific columns of csv file using Pandas 
    context.df2 = pd.read_csv( csv_path, skiprows = lambda x: valid(x), usecols=[1,2,3,4,5,6])
    context.qtrj = context.df2.to_numpy()


    context.nb_exples = int(np.shape(context.results)[0]/6)
    context.results= context.results.reshape(context.nb_exples, 6, 202)#(context.nb_exples, 6, 102)

    context.W = context.results[:, :, 1:101]
    context.taus = context.results[:, :, 101]
    #context.cas = context.results[:, :, 102:202]
    context.qstarts =  context.results[:, :, 0]

    context.goal_qdef =  [-0.39410239854921514, -2.0094973049559535, 1.823418919240133, -1.3935540479472657, -1.583463493977682, 0.34610843658447266]
    context.qgoal = context.qtrj[len(context.qtrj) -1]  
    
    #To execute the Feature just once
    context.execute_once = False  
    
    #Index of the object that will be modified depending on the user's entry value
    context.example_index = None
    
    

def before_feature(context, feature): 
    pass

def after_feature(context, feature):
    if feature.name == "Specific Feature" and context.execute_once == True:
        feature.skip(reason="Feature already executed once")
        
    if feature.name == "Specific Feature" and context.execute_once == False:
        context.execute_once = True


def before_scenario(context, scenario): 
    pass

def after_scenario(context, scenario):
    pass

def after_step(context, scenario):
    pass


#return the estimaed trajectory in C-space for the example "example_index"
def generate_Traj_from_DMPparams(context, tau_value):
    #--- define parameters from the NN 
    q_goal = context.qgoal

    q_start = context.qstarts[context.example_index, :] 
    q_start = np.reshape(q_start, (6,))

    weights = context.W[context.example_index, :, :]
         
    tau = tau_value
    dt  = tau/len(context.qtrj)
    
    #----
    ts = np.arange(0, tau, dt)#dt  = tau/len(context.qtrj)  ts = np.arange(0, tau, dt)#
    
    cs_alpha = -np.log(0.0001)

    ## encode DMP 
    NDOF = 6
    dmp_q = dmp_joint.JointDMP(NDOF = 6,n_bfs=100, alpha=48, beta=12, cs_alpha=cs_alpha)

    #---pre-division - divide weights with the cs values
    
    for i in range(weights.shape[0]):
        weights[i,:] = weights[i,:]/dmp_q.c
     
    #----

    #applying new parameters
    dmp_q.set_trained(weights, dmp_q.c , dmp_q.h, q_start, q_goal) #context.cas[example_index, 0, :]

    """
    print("ts", ts)
    print("de ts", ts[1]-ts[0])
    print("de ts", ts[2]-ts[1])
    print("de ts", ts[6]-ts[5])
    print("len(ts)",len(ts))
    print("tau", tau)
    
    """
    q_out, dq_out, ddq_out = dmp_q.rollout(ts, tau, FX=True)
    #print("len(q_out)", len(q_out))

    timestep = ts[1]-ts[0]
    return q_out, timestep


def PositionName2Index(context, position_name):
    return data["Positions"][position_name]#return th eindex of the example

#real robot perform the first part of traj
def moveRobot2Obj(context, position_name):
    
    context.example_index = PositionName2Index(context, position_name)

    goal_qdef = context.goal_qdef 
    q_start = context.qstarts[context.example_index, :] 
    goal_qAboveObj = np.reshape(q_start, (6,))
    
    try:
        #start trajectory
        if(context.rtde_c.isConnected()):
            #move to home pos
            context.rtde_c.moveJ(goal_qdef)
            
            #moving default to above object 
            context.rtde_c.moveJ(goal_qAboveObj)
            obj_pose = context.rtde_r.getTargetTCPPose()   
            #translation to reach object    
            next_objpose = obj_pose 
            next_objpose[2] = next_objpose[2] - 0.09
            context.rtde_c.moveL(next_objpose)


    except KeyboardInterrupt:

        context.rtde_c.stopScript()
        context.rtde_c.stopScript()


def closeGripper(context):
    
    #close context.gripper
   context.gripper.move(10)
 
def openGripper(context):
     
   context.gripper.open()


def moveRobotFromObj2Place(context):
    
    tau = 15
    
    #trajectory obtained from DMP
    qTraj ,ts = generate_Traj_from_DMPparams(context, tau)
    
    #above object config
    q_start  = context.qstarts[context.example_index, :] 
    goal_qAboveObj = np.reshape(q_start, (6,))
    
    # Parameters
    velocity = 1.05
    acceleration = 1.4
    lookahead_time = 0.03
    gain = 500
    frequency  = 500
    dt = 1 /frequency
          
    try:
        #start trajectory
        if(context.rtde_c.isConnected()):   
            #moving again to above object 
            context.rtde_c.moveJ(goal_qAboveObj)
                    
            #start NN predicted traj
            context.rtde_r.startFileRecording(context.output)
            #print("Data recording started, press [Ctrl-C] to end recording.")
            
            i = 0 
            
            timestart = time.time()
            while i < len(qTraj):
                context.rtde_c.servoJ(qTraj[i], velocity, acceleration, dt, lookahead_time, gain)
                timest = time.time()
                for j in range(40000*tau):
                    pass
                timest2 = time.time()
                #print(timest2 - timest)
                i= i + 1
                
                
            timestop = time.time()
            time.sleep(1)
            
            context.rtde_r.stopFileRecording()
            #print("\nData recording stopped.")
            print("Overall execution time: ", "{:.3f}".format(timestop - timestart), "seconds" )

    except KeyboardInterrupt:
        
        context.rtde_c.stopScript()
        context.rtde_c.stopScript()
        


