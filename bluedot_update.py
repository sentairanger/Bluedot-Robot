#import libraries
from bluedot import BlueDot
from gpiozero import CamJamKitRobot, LED, Button
from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
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

# Define the new camera and the configurations
picam2 = Picamera2()
video_config = picam2.create_video_configuration()
picam2.configure(video_config)
encoder = H264Encoder(10000000)
moment = datetime.now()

#Blink the LED 4 times to ensure the code runs correctly
devastator_eye.blink(n=4)

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

#Define the record and stop_record functions
def record():
    print("recording!")
    picam2.start_recording(encoder, '/home/torvalds/Videos/video2_%02d_%02d_%02d.mjpg' % (moment.hour, moment.minute, moment.second))

def stop_record():
    print("stop recording!")
    picam2.stop_recording()

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