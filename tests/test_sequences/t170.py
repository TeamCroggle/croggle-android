from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import commands
import sys
import os

# Prerequisites:
# - the placement screen is displayed
# - the lambda term that was created in T160 is displayed
#   (other lambda terms might work too)
# This was tested on a device with a display resolution of 1280x720


def calcWidth(width):
	return int(int(displayWidth) * int(width) / int(1280))

def calcHeight(height):
	return int(int(displayHeight) * int(height) / int(720))

print "Starting test sequence T170"

device = MonkeyRunner.waitForConnection()

displayWidth = device.getProperty("display.width")
displayHeight = device.getProperty("display.height")


print "Clicking the 'start simulation' button"
device.touch (calcWidth(1120), calcHeight(500), "DOWN_AND_UP")
MonkeyRunner.sleep(5)

print "Clicking the 'stop simulation' button"
device.touch (calcWidth(1120), calcHeight(500), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Clicking the 'step forward' button"
device.touch (calcWidth(1180), calcHeight(320), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Clicking the 'step backward' button"
device.touch (calcWidth(1040), calcHeight(320), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Increasing the simulation speed"
device.drag ((calcWidth(760), calcHeight(610)),(calcWidth(940), calcHeight(610)), 1, 50)
MonkeyRunner.sleep(2)

print "Clicking the 'start simulation' button"
device.touch (calcWidth(1120), calcHeight(500), "DOWN_AND_UP")
MonkeyRunner.sleep(5)

print "Clicking the 'start simulation' button"
device.touch (calcWidth(1160), calcHeight(60), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Clicking the 'next' button"
device.touch (calcWidth(1150), calcHeight(600), "DOWN_AND_UP")
MonkeyRunner.sleep(3)

print "Clicking the 'ingame menu' button"
device.touch (calcWidth(90), calcHeight(100), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Clicking the 'main menu' button"
device.touch (calcWidth(600), calcHeight(650), "DOWN_AND_UP")
MonkeyRunner.sleep(2)


print "Finishing the test sequence" 


