from behave import when, given, then
import behave
from behave.model_core import Status
import time
import environment as env 
import os
import json

@then(u'the "position" of the robot "{identifier}" is "{position}"')
@given(u'the "position" of the robot "{identifier}" is "{position}"')
@then(u'the position of the robot "{identifier}" is "{position}"')
@given(u'the position of the robot "{identifier}" is "{position}"')
def step_impl(context, identifier : str, position):  
    
    #check if robot is already in a correct position 
    if(env.actual_pos == position):
        pass
    else :
        env.actual_pos = env.moveRobot(context, position)


@when(u'the robot "{identifier1}" {action1} the object "{identifier2}"')
def step_impl(context, identifier1 :str, identifier2:str, action1):
    
    if (action1 == "grabs"):
        env.magnet_state = env.activateMagnet(context)
    
    if (action1 == "moves"):
        print("\t Error from user : \"moves\" can only be used for moving the robot itself")
        raise("Error from user : \"moves\" can only be used for moving the robot itself")



@given(u'the color of the object "{identifier}" is "{color_state}"')
def step_impl(context, identifier : str, color_state):

    #Check if the color mentioned same as the one sensed 
    if(env.obj_color_sensed != color_state):
        print("\t SKIPPING SCENARIO BECAUSE INCORRECT COLOR")
        print("\t DETECTED COLOR:", env.obj_color_sensed)
        context.scenario.skip("Skipping scenario because condition is not met")
        


@when('the robot "{identifier}" moves to position "{position}"')
def step_when(context, identifier : str, position):
    
    env.actual_pos = env.moveRobot(context, position)


@given('the object "{identifier}" is {state}')
@then('the object "{identifier}" is {state}')
def step_impl(context, identifier : str, state):
            
    if (state == "released"):
        env.magnet_state = env.deactivateMagnet(context)
        
    if (state == "sensed"):
            env.obj_color_sensed = env.detectColor(context)



