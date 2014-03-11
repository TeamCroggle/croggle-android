from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import commands
import sys
import os

# Prerequisites:
# - the main menu screen is displayed
# - there is an active profile
# This was tested on a device with a display resolution of 1280x720

def calcWidth(width):
	return int(int(displayWidth) * int(width) / int(1280))

def calcHeight(height):
	return int(int(displayHeight) * int(height) / int(720))

print "Starting test sequence T130"

device = MonkeyRunner.waitForConnection()

displayWidth = device.getProperty("display.width")
displayHeight = device.getProperty("display.height")

print "Clicking the 'setting' button"
device.touch (calcWidth(100), calcHeight(620), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Clicking the 'edit profile' button"
device.touch (calcWidth(400), calcHeight(610), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Clicking the 'edit profile name' button"
device.touch (calcWidth(250), calcHeight(510), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Clicking the text field"
device.touch (calcWidth(600), calcHeight(310), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Presing the letter g"
device.touch (calcWidth(650), calcHeight(528),"DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Closing the on-screen keyboard"
device.touch (calcWidth(1210), calcHeight(670), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Clicking the 'next' button"
device.touch (calcWidth(960), calcHeight(470), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Clicking the 'edit profile' button"
device.touch (calcWidth(400), calcHeight(610), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Clicking the 'edit profile picture' button"
device.touch (calcWidth(500), calcHeight(500), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Selecting the green crocodile"
device.touch (calcWidth(600), calcHeight(400), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Clicking the 'next' button"
device.touch (960, calcHeight(470), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Clicking the 'back' button"
device.touch (calcWidth(100), calcHeight(90), "DOWN_AND_UP")
MonkeyRunner.sleep(2)



print "Finishing the test sequence" 
