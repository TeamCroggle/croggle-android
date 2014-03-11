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

print "Starting test sequence T150"

device = MonkeyRunner.waitForConnection()

displayWidth = device.getProperty("display.width")
displayHeight = device.getProperty("display.height")

print "Clicking the 'play' button"
device.touch (calcWidth(450.3) , calcHeight(350), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Selecting a level package"
device.touch (calcWidth(400), calcHeight(400), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Selecting the first level"
device.touch (calcWidth(350), calcHeight(160), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Finishing the test sequence" 
