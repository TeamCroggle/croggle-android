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

print "Starting test sequence T140"

device = MonkeyRunner.waitForConnection()

displayWidth = device.getProperty("display.width")
displayHeight = device.getProperty("display.height")

print "Clicking the 'setting' button"
device.touch (calcWidth(100) , calcHeight(620), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Clicking the 'edit profile' button"
device.touch (calcWidth(400), calcHeight(610), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Clicking the 'delete profile' button"
device.touch (calcWidth(800), calcHeight(510), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Clicking the 'ok' button"
device.touch (calcWidth(430), calcHeight(530), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Selecting one user"
device.touch (calcWidth(640), calcHeight(320), "DOWN_AND_UP")
MonkeyRunner.sleep(2)



print "Finishing the test sequence" 
