from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import commands
import sys
import os

# Prerequisites
# - level 1 package 1 is freshly loaded into the placement screen
# - the level is played with a freshly created profile

# This was tested on a device with a display resolution of 1280x720
# Sometimes an error appears while running a test case for the first time, restarting it usually solves this problem


def calcWidth(width):
	return int(int(displayWidth) * int(width) / int(1280))

def calcHeight(height):
	return int(int(displayHeight) * int(height) / int(720))

print "Starting test sequence T210"

device = MonkeyRunner.waitForConnection()

displayWidth = device.getProperty("display.width")
displayHeight = device.getProperty("display.height")


print "Closing the tutorial"
device.touch (calcWidth(1020), calcHeight(560), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Closing the tutorial"
device.touch (calcWidth(1020), calcHeight(560), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Closing the tutorial"
device.touch (calcWidth(1020), calcHeight(560), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Closing the tutorial"
device.touch (calcWidth(1020), calcHeight(560), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Opening the 'goal board' pop up"
device.touch (calcWidth(100), calcHeight(400), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Closing the 'goal board' pop up"
device.touch (calcWidth(1080), calcHeight(400), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Clicking the uncolored egg"
device.touch (calcWidth(600), calcHeight(100), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Selecting a color"
device.touch (calcWidth(690), calcHeight(350), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Clicking the 'play' button"
device.touch (calcWidth(1140), calcHeight(500), "DOWN_AND_UP")
MonkeyRunner.sleep(3)

print "Clicking the 'step forward' button"
device.touch (calcWidth(1180), calcHeight(320), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Clicking the 'step forward' button"
device.touch (calcWidth(1180), calcHeight(320), "DOWN_AND_UP")
MonkeyRunner.sleep(4)

print "Clicking the 'achievements' button"
device.touch (calcWidth(120), calcHeight(600), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Closing the 'achievements' pop up"
device.touch (calcWidth(930), calcHeight(600), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Clicking the 'level menu' button"
device.touch (calcWidth(810), calcHeight(600), "DOWN_AND_UP")
MonkeyRunner.sleep(2)



print "Finishing the test sequence" 
