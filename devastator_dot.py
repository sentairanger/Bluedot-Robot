#import libraries
from bluedot import BlueDot
from gpiozero import CamJamKitRobot, LED, Button
from picamera import PiCamera
from datetime import datetime
from signal import pause
import os
from time import sleep

#setup robot, blue dot, LED, and the two button variables
devastator_bluedot = BlueDot()
devastator_robot = CamJamKitRobot()
devastator_eye = LED(25)
record_button = Button(13)
stop_button = Button(21)

#Setup the camera Variables
devastator_camera = PiCamera()
devastator_camera.resolution = (1280, 720)
devastator_camera.framerate = 25
moment = datetime.now()

#Blink the LED 4 times to ensure the code runs correctly
for x in range(1, 5):
    devastator_eye.off()
    sleep(0.5)
    devastator_eye.on()
    sleep(0.5)

#Define the move function and the individual commands
def move(pos):
    if pos.top:
        devastator_robot.forward()
    elif pos.bottom:
        devastator_robot.backward()
    elif pos.left:
        devastator_robot.left()
    elif pos.right:
        devastator_robot.right()
    elif pos.middle:
        os.system("sudo shutdown now")

#Define the stop and record functions 
def stop():
    devastator_robot.stop()

def record():
    devastator_eye.off()
    devastator_camera.start_recording('/home/pi/Videos/motions_%02d_%02d_%02d.mjpg' % (moment.hour, moment.minute, moment.second))

def stop_record():
    devastator_eye.on()
    devastator_camera.stop_recording()

#When the dot is pressed the robot moves
#When the dot is released it stops
#When pressing one button the camera turns on
#When the other button is pressed the camera turns off
devastator_bluedot.when_pressed = move
devastator_bluedot.when_moved = move
devastator_bluedot.when_released = stop
record_button.when_pressed = record
stop_button.when_pressed = stop_record

pause()
