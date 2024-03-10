from behave import when, given, then
import behave
from behave.model_core import Status
import time
import environment as env 
import os
import json

@given(u'the object "{identifier}" is {state}')
@then(u'the object "{identifier}" is {state}')
@given(u'the object "{identifier}" is "{state}"')
@then(u'the object "{identifier}" is "{state}"')
def step_impl(context, identifier : str, state):
    if(state == "fixed"):
        print("Object ready to be grabbed")
    if(state == "placed"):
        env.openGripper(context)
        print("Object placed")


@when('the robot "{identifier}" moves to position "{position}"')
def step_when(context, identifier : str, position):
    if(position[:3] == 'POS'):# check the first 3 letters
        env.moveRobot2Obj(context, position)
    if(position == "Bucket"):
        env.moveRobotFromObj2Place(context)


@when(u'the robot "{identifier1}" {action} the object "{identifier2}"')
def step_impl(context, identifier1 :str, identifier2:str, action):
    env.closeGripper(context)
    print("Object grabbed")



