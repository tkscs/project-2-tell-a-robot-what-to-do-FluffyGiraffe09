
# 3 input function prompts with
### 2 possible user responses each
### 5 sonar readings
### some possibility of indefinite repetition (using a while loop or recursion)

#--------------------------------------------------------------------------------------------

# Robot can move, and code runs without errors in simulator
# Robot does not crash into walls

# At least one if/elif/else chain with 3+ branches
# At least one if/else that checks a sonar sensor reading
# At least one if/else that checks user input

# At least 3 different input() prompts
# At least 6 different user responses are handled (2 per prompt above)
# Robot behavior changes based on user input at least 6 times (each response above corresponds to a different behavior)

# Define at least 3 functions
# Call each of your functions at least once
# For each function, include a doc string explaining the API
# At least 1 of your functions has at least 1 parameter

# Read a sonar distance at least 5 times
# Robot behavior changes based on the sonar values

# Implements indefinite execusing using at least one while loop OR at least one recursive function call
# There is an option to terminate your indefinite execution
from simulator import robot, FORWARD, BACKWARD, STOP
# TODO: Write your code here!

def go(seconds):
    robot.motors(FORWARD, FORWARD, seconds)

def back(seconds):
    robot.motors(BACKWARD, BACKWARD, seconds)

def right(seconds):
    robot.motors(BACKWARD, FORWARD, seconds)

def left(seconds):
    robot.motors(FORWARD, BACKWARD, seconds)

def is_float(x):
    try:
        float(x)
        return True
    except ValueError:
        return False
def spin_right():
    x=input("How long would you like me to spin for (between 1 and 6 seconds) ?")
    if is_float(x) == False:
        print("That is not a valid response :/")
        spin_right()
    elif 1<= float(x) <=6:
        x=float(x)
        right(x)
        start()
    elif 1> float(x) or  float(x)>6:
        x=float(x)
        print("You must pick a number within the bounds")
        spin_right()
def spin_left():
    x=input("How long would you like me to spin for (between 1 and 6 seconds) ?")
    if is_float(x) == False:
        print("That is not a valid response :/")
        spin_left()
    elif 1<= float(x) <=6:
        x=float(x)
        left(x)
        start()
    elif 1> float(x) or  float(x)>6:
        x=float(x)
        print("You must pick a number within the bounds")
        spin_left()
def dance():
    for i in range(2):
        go(2)
        right(2)
        left(2)
        back(2)
        right(2)
        left(2)
    start()
def chacha_slide():
    slide_left()
    slide_right()
    2 criss_cross()
    chacha()

def start():
    response=input("Hi! I am a Robot! Would you like to see me do a trick?")
    if response=="yes":
        response=input("What trick would you like to see? I can do a spin to the right (1), a spin to the left (2), a little dance (3), and the chacha slide().")
        if response=="1":
            spin_right()
        elif response=="2":
            spin_left()
        elif response=="3":
            dance()
        elif response=="4":
            chacha_slide()
        else:
            print("Please respond with one of the options.")
    elif response=="no":
        print("See you next time!")
    else:
        print("since you did not respond yes or no, I a going to do my favorite trick!")
        dance()

start()


    

# left_distance = robot.left_sonar()
# right_distance = robot.right_sonar()
# while True:
#     left_distance
#     if left_distance<10 or right_distance<10:
#         robot.motors(STOP, STOP)
#         back(10)
#         break
#         False
#     go(5)
#     right(3)
#     go(7)
    




# Use robot.motors() to move
# Use robot.left_sonar() and robot.right_sonar()) to sense obstacles

# When you're done, close the simulator
robot.exit()

