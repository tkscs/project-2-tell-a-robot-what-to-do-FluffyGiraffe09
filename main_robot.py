from simulator import robot, FORWARD, BACKWARD, STOP
# TODO: Write your code here!

def go(seconds):
    """
    This function goes FORWARD.
    The parameter is seconds:
        any number that tells the robot to go forward for a certain amount of seconds
    """
    robot.motors(FORWARD, FORWARD, seconds)

def back(seconds):
    """
    This function goes BACKWARD.
    The parameter is seconds:
        any number that tells the robot to go backward for a certain amount of seconds
    """
    robot.motors(BACKWARD, BACKWARD, seconds)

def right(seconds):
    """
    This function TURNS RIGHT.
    The parameter is seconds:
        any number that tells the robot to turn right for a certain amount of seconds
    """
    robot.motors(BACKWARD, FORWARD, seconds)

def left(seconds):
    """
    This function TURNS LEFT.
    The parameter is seconds:
        any number that tells the robot to turn left for a certain amount of seconds
    """
    robot.motors(FORWARD, BACKWARD, seconds)

Block = "No"

    
left_distance = robot.left_sonar()
right_distance = robot.right_sonar()

def how_far():
    """
    This function checks HOW FAR AWAY the robot is from an object or the wall
    If the robot is less than 20 cm away from an object it will go back for 10 seconds
    """
    left_distance = robot.left_sonar()
    right_distance = robot.right_sonar()
    if left_distance<20 or right_distance<20:
        robot.motors(STOP, STOP, 1)
        back(10)

def is_float(x):
    """
    This function CHECKS whether or not the INPUT IS A NUMBER
    When the person is asked how long they would like the robot to turn for, the input is checked to make sure it is a number.
    If it is not a number, the code will say that it is not a valid response and it will ask again.
    If it is a number, the code will continue.
    """
    try:
        float(x)
        return True
    except ValueError:
        return False
def spin_right():
    """
    This function is one of the tricks that the robot can do: it SPINS TO THE RIGHT.
    It also asks how long it should spin to the right for and it checks how far it is from the wall so that it doesn't crash.
    At the end of the function, it goes back to the starting function.
    """
    left_distance = robot.left_sonar()
    right_distance = robot.right_sonar()
    x=input("How long would you like me to spin for (between 1 and 6 seconds) ?")
    if is_float(x) == False:
            print("That is not a valid response :/")
            return spin_right()
    elif 1 <= float(x) <= 6:
            x=float(x)
            for i in range(90):
                left_distance = robot.left_sonar()
                right_distance = robot.right_sonar()
                if left_distance > 5 and right_distance > 5:
                    Block = "No"
                    right(float(x) / 90)
                elif left_distance <= 5 or right_distance <= 5:
                    Block = "Yes"
                    break
            start()
            if Block == "Yes":
                print("Uh oh! There's something in my way.")
                back(10)
                return spin_right()
    elif 1> float(x) or  float(x)>6:
            x=float(x)
            print("You must pick a number within the bounds")
            return spin_right()
def spin_left():
    """
    This function is one of the tricks that the robot can do: it SPINS TO THE LEFT.
    It also asks how long it should spin to the left for and it checks how far it is from the wall so that it doesn't crash.
    At the end of the function, it goes back to the starting function.
    """
    left_distance = robot.left_sonar()
    right_distance = robot.right_sonar()
    x=input("How long would you like me to spin for (between 1 and 6 seconds) ?")
    if is_float(x) == False:
            print("That is not a valid response :/")
            return spin_left()
    elif 1 <= float(x) <= 6:
            x=float(x)
            for i in range(90):
                left_distance = robot.left_sonar()
                right_distance = robot.right_sonar()
                if left_distance > 5 and right_distance > 5:
                    Block = "No"
                    left(float(x) / 90)
                elif left_distance <= 5 or right_distance <= 5:
                    Block = "Yes"
                    break
            start()
            if Block == "Yes":
                print("Uh oh! There's something in my way.")
                back(10)
            return spin_left()
    elif 1> float(x) or  float(x)>6:
            x=float(x)
            print("You must pick a number within the bounds")
            return spin_left()
def dance():
    """
    This function does A LITTLE DANCE.
    It also checks to make sure that it won't crash into the wall.
    At the end of the function, it returns back to the starting code.
    """
    how_far()
    for i in range(2):
        go(2)
        right(1)
        left(2)
        back(2)
        right(1)
        left(2)
    start()
def chacha_slide():
    """
    This function does A PART OF THE CHACHA SLIDE.
    It also checks to make sure that it won't crash into the wall.
    At the end of the function, it returns back to the starting code.
    """
    how_far()
    left(1.525)
    # slide_left()
    left(1.525)
    go(1)
    # slide_right()
    right(3.05)
    go(1)
    left(1.525)
    # 2 criss_cross()
    left(0.5)
    right(1)
    left(1)
    right(0.5)
    # chacha (real smooth)
    for i in range(3):
        go(1)
        back(1)
    start()
def start():
    """
    THIS FUNCTION IS THE STARTING CODE THAT INTERACTS WITH THE HUMAN. 
    IT ASKS IF THE PERSON WOULD LIKE TO SEE A TRICK AND IF SO WHAT TRICK THEY WOULD LIKE TO SEE.
    """
    response=input("Hi! I am a Robot! Would you like to see me do a trick? (yes, or no)")
    if response=="yes" or response=="Y" or response=="Yes" or response=="y":
        response=input("What trick would you like to see? I can do a spin to the right (1), a spin to the left (2), a little dance (3), and the chacha slide (4).")
        if response=="1" or response=="spin right":
            spin_right()
        elif response=="2" or response=="spin left":
            spin_left()
        elif response=="3" or response=="little dance":
            dance()
        elif response=="4" or response=="cha cha slide":
            chacha_slide()
        else:
            print("Please respond with one of the options.")
            start()
    elif response=="no":
        print("See you next time!")
        robot.exit()
    else:
        start()


how_far()
start()

    


# When you're done, close the simulator
robot.exit()

