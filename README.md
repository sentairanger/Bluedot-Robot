# Bluedot-Robot

## Overview of Project

This project is similar to [this](https://github.com/sentairanger/Camera-Robot) previous project I did with my robot Torvalds, but this time using the Bluedot App. 

### Getting Started

To get things started the same process will be repeated for this robot as with my Camera-Robot project. So let's get started.

Hardware Requirements:
* Raspberry Pi: Can be any Pi you want as long as you provide enough power and has bluetooth. I used the Zero W in this case because it was smaller and used less power. 
* Micro SD card.
* Bluetooth keyboard/mouse controller. You can use a USB version if you want.
* Keyboard and Mouse for initial setup
* USB Power Bank or UBEC
* Robot Chassis: Can be any you want. I chose the Devastator Tank Mobile Platform from DF Robot. 
* Battery Pack for the motors.
* Pi Camera and Ribbon Cable: Use the Zero ribbon cable if you are using the Zero W.
* Two HDD LEDs for optional eyes or use LEDs as indicators. Be sure to add resistors and dupont cables as they will be needed.
* Optional 3D Printed Mount for the Camera. Go [here](https://www.youtube.com/redirect?v=pK0XvjiP2qk&event=video_description&q=https%3A%2F%2Fwww.tinkercad.com%2Fthings%2Fhn6jajTg5Sv-pidevcammount&redir_token=5HilQU2EE7I65Pj-rn8G7S3pxvl8MTU4NDQ5MDk4MEAxNTg0NDA0NTgw)

Software Requirements:
* Raspbian: Go [here](https://www.raspberrypi.org/downloads/raspbian/)
* This repository
* BlueDot App: Download on Google Play

### Starting up the Robot

Here are the steps to take to get the robot running and recording:

1. Assemble Robot with the Camera.
2. Insert Micro SD card into a card reader on your PC or laptop and install Raspbian using an image writer like etcher or the new Rasbperry Pi Imager.
3. Insert Micro SD card into your Pi.
4. Install Bluedot on your Phone or Tablet. Make sure your Camera is enabled by going to Menu > Preferences > Raspberry Pi Configuration > Interfaces > Camera > Enable.
5. Temporarily connect Robot to a monitor, keyboard and mouse.
6. Go to the terminal and clone this repository. 
7. Move the repository to the Documents directory to make things easier.
8. Enable bluetooth on your Pi and pair your devices. Once that is setup go to the Documents directory and run the code like so: `python devastator_dot.py`.
9. Your robot should now move forward, backwards, left and right based on where you press the dot. Also press one of the buttons to start recording video.
10. Press the middle of the dot to ensure a graceful shutdown. And with that your robot has worked.

### Running the Robot on Boot

To make sure the robot can run the robot on boot, I have included the `bluedot_bootup.sh` to ensure that it works. The process is the same as my Camera-Robot project. First, go to a termnal and change to the directory where you have the repository cloned. Type `chmod +x bluedot_bootup.sh` to ensure the script is executable. Then type `cd /etc/xdg/lxsession/LXDE-pi` to edit the autostart file. Type `sudo nano autostart` to edit the file. At the end of the line type `@lxterminal -e /home/pi/Documents/Bluedot-Robot/bluedot_bootup.sh` to execute the code on boot. Then go to the Menu > Preferences > Raspberry Pi Configuration > Resolution. Set the Resolution to anything other than default. Reboot and the code should now run. 
