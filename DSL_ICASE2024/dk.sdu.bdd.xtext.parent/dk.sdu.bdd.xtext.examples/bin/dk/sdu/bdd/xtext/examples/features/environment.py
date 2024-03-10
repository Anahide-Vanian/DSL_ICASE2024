#from behave import fixture
import json
from behave.model import Scenario
#Libraries linked with Arduino 
import sys, time
import random
import serial
import io

f = open("Environment.json")
data = json.load(f)


#Global variables
actual_pos  = "default"
obj_color_sensed = "None"
magnet_state = "OFF"
already_sensed = False

        
def before_all(context):
    print("Setting up Environment...")
    # Send setup command to Arduino
    
    context.serial_port = "COM9"

    context.curSerial = serial.Serial(context.serial_port, 115200, timeout=1)
    
    time.sleep(2)
    
    #motor speeds
    context.speed1 = 500
    context.speed2 = 200
    context.speed3 = 300
    context.speed4 = 500
    
    #To execute the Feature just once
    context.execute_once = False  
    

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


#move the robot and return position to update the global variables in tests.py
def moveRobot(context, position):
    
    target_angles = position2MotorAngles(position)    

    #before action put two servos in safe config
    
    text2 = "{\"cmd\":\"setServoPos\",\"value\": 500, \"speed\":" + str(context.speed2) +", \"id\":2}"  
    writeText2SerialPort(context, text2)#motor 2
    time.sleep(0.2)
      
    #move the robot
    text1 = "{\"cmd\":\"begin\”}" 
    text2 = "{\"cmd\": \"setServoPos\",\"value\": " + str(target_angles[0]) + ", \"speed\":" + str(context.speed1) +", \"id\":1}"
    text3 = "{\"cmd\":\"setServoPos\",\"value\": " + str(target_angles[1]) + ",  \"speed\":" + str(context.speed2) +", \"id\":2}"
    text4 = "{\"cmd\":\"setServoPos\",\"value\": " + str(target_angles[2]) + ",  \"speed\":" + str(context.speed3) +",\"id\":3}" 
    text5 = "{\"cmd\":\"setServoPos\",\"value\": " + str(target_angles[3]) + ",  \"speed\":" + str(context.speed4) +",\"id\":4}"
    text6 = "{\"cmd\":\"end\”}"
  
    writeText2SerialPort(context, text1) 
    time.sleep(0.5)
    writeText2SerialPort(context, text2)#motor 1
    time.sleep(0.5)
    writeText2SerialPort(context, text4)#motor 3
    time.sleep(0.5)  
    writeText2SerialPort(context, text5)#motor 4 first to avoid collision 
    time.sleep(0.5)
    writeText2SerialPort(context, text3)#motor 2 first to avoid collision 
    time.sleep(0.5)
    writeText2SerialPort(context, text6)
    
    return position
    
    
    
def deactivateMagnet(context):
    
    # we activate the magnet
    text = "{\"cmd\":\"setRelay\",\"value\":false}"
    
    writeText2SerialPort(context, text)
    time.sleep(0.2)
    
    #update global variable
    return "OFF"
    
    
def activateMagnet(context):
    
    # we activate the magnet
    text = "{\"cmd\":\"setRelay\",\"value\":true}"
    
    writeText2SerialPort(context, text)
    time.sleep(0.2)
    
    #update global variable
    return "ON"
    
        
def detectColor(context):
    
    # Construct the JSON command with proper formatting
    command = "{\"cmd\": \"getColor\"}"
    
    # Write the JSON command to the serial port
    writeText2SerialPort(context, command)
    #time.sleep(0.5)
    
    # Read the response from the serial port
    response_dict = readTextFromSerialPort(context)
    
    # Extract the "value" from the response
    r_value = response_dict.get("r")
    g_value = response_dict.get("g")
    b_value = response_dict.get("b")
    
    
    if(r_value > g_value and r_value > b_value):
        obj_color_sensed = "red"
        print("\t THE OBJECT IS RED")#save it to context variable    
    elif(g_value > r_value and g_value > b_value):
        obj_color_sensed = "green"
        print("\t THE OBJECT IS GREEN")      
    elif(b_value > r_value and b_value > g_value):
        obj_color_sensed = "blue"
        print("\t THE OBJECT IS BLUE")
        
    return obj_color_sensed
        
  
    
def position2MotorAngles(name):
    locations = data["Positions"]
    coordinate = locations[name]

    return coordinate



def writeText2SerialPort(context, text):
 
    context.curSerial.write(text.encode())
    time.sleep(1)
    
def readTextFromSerialPort(context):
 

    while True:
        # Read a line from the serial port
        line = context.curSerial.readline().decode().strip()
        
        # Check if the line is not empty
        if line:
            # Print the received data
            #print('Received from Arduino:', line)
            parsed_json = json.loads(line)#transforms strings to dictionary
            
            if(parsed_json.get("cmd") == "debug" or parsed_json.get("value") == -1):
                continue 
            else:
                return parsed_json

    




