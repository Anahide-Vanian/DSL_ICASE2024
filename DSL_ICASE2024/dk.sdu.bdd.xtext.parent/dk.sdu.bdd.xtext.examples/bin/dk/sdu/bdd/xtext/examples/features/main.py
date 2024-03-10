from behave.__main__ import main as behave_main

from logic.fileReader import readFile
import time
import os

def main():
    readFile()
    path = os.path.join(os.path.dirname(__file__))
    # path = C:\Users\ansil\eclipse-workspace\DSLBeta1-robot\dk.sdu.bdd.xtext.parent\dk.sdu.bdd.xtext.examples\src\dk\sdu\bdd\xtext\examples\features
    # __file__ is a special variable that holds the path of the current Python script.
    # os.path.dirname(__file__) gets the directory name of the current script's (or module's) file.
    
    # os.path.join() is used to join one or more path components intelligently.
    # In this case, it's used to join the current script's directory with an empty string, effectively giving the current script's directory.
    
    # Starts test
    behave_main([path] + ["--stop", "--no-capture"])#executes the ".feature" file which means run the methods associated to each steps listed in the file written using the Gherkin Syntax (tests.py)

if __name__ == '__main__':
    main() 
    
    
      
    
"""



Scenario: "4"
Given the position of the robot "Bent" is "SENSOR_AREA"
When the object "Blue" sensed to color "blue"
Then the "position" of the robot "Bent" is "SENSOR_AREA"




//Scenario: "3"
//Given the position of the robot "Bent" is "SENSOR_AREA"
//When the sensor "Sensor" to color "blue"
//And the robot "Bent" moves to position "SENSOR_AREA"
//Then the "position" of the robot "Bent" is "SENSOR_AREA"

####
Scenario: "Grabbing and sensing the object"
Given the position of the robot "Robot" is "default"
When the robot "Robot" moves to position "START_1"
And the robot "Robot" grabs the object "Cube"
And the robot "Robot" moves to position "SENSOR_AREA"
Then the object "Cube" is sensed

Scenario: "Sorting the object to its corresponding bucket"
Given the color of the object "Cube" is "red"
And the object "Cube" is sensed
When the robot "Robot" moves to position "RED_BUCKET"
Then the object "Cube" is released

Scenario: "Sorting the object to its corresponding bucket"
Given the color of the object "Cube" is "green"
And the object "Cube" is sensed
When the robot "Robot" moves to position "GREEN_BUCKET"
Then the object "Cube" is released

Scenario: "Sorting the object to its corresponding bucket"
Given the color of the object "Cube" is "blue"
When the robot "Robot" moves to position "BLUE_BUCKET"
Then the object "Cube" is released

//OBJ2
Scenario: "Grabbing and sensing the object"
Given the position of the robot "Robot" is "default"
When the robot "Robot" moves to position "START_2"
And the robot "Robot" grabs the object "Cube"
And the robot "Robot" moves to position "SENSOR_AREA"
Then the object "Cube" is sensed

Scenario: "Sorting the object to its corresponding bucket"
Given the color of the object "Cube" is "red"
When the robot "Robot" moves to position "RED_BUCKET"
Then the object "Cube" is released

Scenario: "Sorting the object to its corresponding bucket"
Given the color of the object "Cube" is "green"
When the robot "Robot" moves to position "GREEN_BUCKET"
Then the object "Cube" is released

Scenario: "Sorting the object to its corresponding bucket"
Given the color of the object "Cube" is "blue"
When the robot "Robot" moves to position "BLUE_BUCKET"
Then the object "Cube" is released

//OBJ3
Scenario: "Grabbing and sensing the object"
Given the position of the robot "Robot" is "default"
When the robot "Robot" moves to position "START_3"
And the robot "Robot" grabs the object "Cube"
And the robot "Robot" moves to position "SENSOR_AREA"
Then the object "Cube" is sensed

Scenario: "Sorting the object to its corresponding bucket"
Given the color of the object "Cube" is "red"
When the robot "Robot" moves to position "RED_BUCKET"
Then the object "Cube" is released

Scenario: "Sorting the object to its corresponding bucket"
Given the color of the object "Cube" is "green"
When the robot "Robot" moves to position "GREEN_BUCKET"
Then the object "Cube" is released

Scenario: "Sorting the object to its corresponding bucket"
Given the color of the object "Cube" is "blue"
When the robot "Robot" moves to position "BLUE_BUCKET"
Then the object "Cube" is released
 


//Step 2: Stacking the objects (red, blue, green order)
Scenario: "Stacking the red object"
Given the position of the robot "Robot" is "default"
When the robot "Robot" moves to position "RED_BUCKET"
And the robot "Robot" grabs the object "Cube"
And the robot "Robot" moves to position "ASSEMBLY_AREA"
Then the object "Cube" is released

Scenario: "Stacking the blue object"
Given the position of the robot "Robot" is "default"
When the robot "Robot" moves to position "BLUE_BUCKET"
And the robot "Robot" grabs the object "Cube"
And the robot "Robot" moves to position "ASSEMBLY_AREA"
Then the object "Cube" is released

Scenario: "Stacking the green object"
Given the position of the robot "Robot" is "default"
When the robot "Robot" moves to position "GREEN_BUCKET"
And the robot "Robot" grabs the object "Cube"
And the robot "Robot" moves to position "ASSEMBLY_AREA"
Then the object "Cube" is released






"""