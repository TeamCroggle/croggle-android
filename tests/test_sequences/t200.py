from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import commands
import sys
import os

# Prerequisites:
# - level 4 in package 2 is loaded freshly into the placement screen 
#   (any other multiple choice level that does not have a tutorial will probably work fine too)
# - there is an active profile

# This was tested on a device with a display resolution of 1280x720
# Sometimes an error appears while running a test case for the first time, restarting it usually solves this problem


def calcWidth(width):
	return int(int(displayWidth) * int(width) / int(1280))

def calcHeight(height):
	return int(int(displayHeight) * int(height) / int(720))

print "Starting test sequence T200"

device = MonkeyRunner.waitForConnection()

displayWidth = device.getProperty("display.width")
displayHeight = device.getProperty("display.height")


print "Closing the goal board pop up"
device.touch (calcWidth(1080), calcHeight(640), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Clicking the 'play' button"
device.touch (calcWidth(1140), calcHeight(500), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Clicking the 'okay' button"
device.touch (calcWidth(640), calcHeight(520), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Selecting the second answer"
device.touch (calcWidth(670), calcHeight(90), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Selecting the third answer"
device.touch (calcWidth(1020), calcHeight(90), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Opening the goal board pop up"
device.touch (calcWidth(100), calcHeight(260), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Closing the goal board pop up"
device.touch (calcWidth(1080), calcHeight(640), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Selecting the first answer"
device.touch (calcWidth(330), calcHeight(90), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Clicking the 'play' button"
device.touch (calcWidth(1140), calcHeight(500), "DOWN_AND_UP")
MonkeyRunner.sleep(3)

print "Clicking the 'play' button"
device.touch (calcWidth(1140), calcHeight(500), "DOWN_AND_UP")
MonkeyRunner.sleep(20)

print "Clicking the 'restart' button"
device.touch (calcWidth(1150), calcHeight(600), "DOWN_AND_UP")
MonkeyRunner.sleep(2)


print "Finishing the test sequence" 


