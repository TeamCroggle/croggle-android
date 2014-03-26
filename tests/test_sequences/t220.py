from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import commands
import sys
import os

# Prerequisites:
# - the main menu screen is displayed
# - there is an active profile

# This was tested on a device with a display resolution of 1280x720
# Sometimes an error appears while running a test case for the first time, restarting it usually solves this problem


def calcWidth(width):
	return int(int(displayWidth) * int(width) / int(1280))

def calcHeight(height):
	return int(int(displayHeight) * int(height) / int(720))

print "Starting test sequence T220"

device = MonkeyRunner.waitForConnection()

displayWidth = device.getProperty("display.width")
displayHeight = device.getProperty("display.height")

print "Clicking the 'achievement' button"
device.touch (calcWidth(760), calcHeight(600), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Moving the screen camera"
device.drag ((calcWidth(600), calcHeight(250)), (calcWidth(600), calcHeight(600)), 0.00001, 50)
MonkeyRunner.sleep(2)

print "Selecting an achievement"
device.touch (calcWidth(230), calcHeight(230), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Closing the pop up"
device.touch (calcWidth(640), calcHeight(500), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Moving the screen camera"
device.drag ((calcWidth(600), calcHeight(600)), (calcWidth(600), calcHeight(100)), 0.00001, 50)
MonkeyRunner.sleep(2)

print "Selecting an achievement"
device.touch (calcWidth(1050), calcHeight(580), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Closing the pop up"
device.touch (calcWidth(640), calcHeight(500), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Clicking the back button"
device.touch (calcWidth(100), calcHeight(100), "DOWN_AND_UP")
MonkeyRunner.sleep(2)



print "Finishing the test sequence" 
