from simulator import robot, FORWARD, BACKWARD, STOP
# TODO: Write your code here!

def go(seconds):
    robot.motors(FORWARD, FORWARD, seconds)

def back(seconds):
    robot.motors(BACKWARD, BACKWARD, seconds)

def right(seconds):
    robot.motors(STOP, FORWARD, seconds)

def left(seconds):
    robot.motors(FORWARD, STOP, seconds)

left_distance = robot.left_sonar()
right_distance = robot.right_sonar()
while True:
    left_distance
    if left_distance<10 or right_distance<10:
        robot.motors(STOP, STOP)
        back(10)
        break
        False
    go(5)
    right(3)
    go(7)
    




# Use robot.motors() to move
# Use robot.left_sonar() and robot.right_sonar()) to sense obstacles

# When you're done, close the simulator
robot.exit()

