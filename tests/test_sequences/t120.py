from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import commands
import sys
import os

# Prerequisites:
# - the main menu screen is displayed
# - there are exactly two profiles stored

# This was tested on a device with a display resolution of 1280x720
# Sometimes an error appears while running a test case for the first time, restarting it usually solves this problem

def calcWidth(width):
	return int(int(displayWidth) * int(width) / int(1280))

def calcHeight(height):
	return int(int(displayHeight) * int(height) / int(720))

print "Starting test sequence T120"

device = MonkeyRunner.waitForConnection()

displayWidth = device.getProperty("display.width")
displayHeight = device.getProperty("display.height")

print "Clicking the 'user' button"
device.touch (calcWidth(1070), calcHeight(330), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Selecting a user"
device.touch (calcWidth(600), calcHeight(360), "DOWN_AND_UP")
MonkeyRunner.sleep(2)


print "Finishing the test sequence" 
