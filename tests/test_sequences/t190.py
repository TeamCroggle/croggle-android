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

print "Starting test sequence T190"

device = MonkeyRunner.waitForConnection()

displayWidth = device.getProperty("display.width")
displayHeight = device.getProperty("display.height")

print "Clicking the 'setting' button"
device.touch (calcWidth(100), calcHeight(620), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Enabling the zoom button"
device.touch (calcWidth(890), calcHeight(170), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Enabling the colorblind mode"
device.touch (calcWidth(890), calcHeight(240), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Turning down the music volume"
device.drag ((calcWidth(1000), calcHeight(380)), (calcWidth(720), calcHeight(380)), 1, 50)
MonkeyRunner.sleep(2)

print "Turning up the effects volume"
device.drag ((calcWidth(720), calcHeight(450)), (calcWidth(1000), calcHeight(450)), 1, 50)
MonkeyRunner.sleep(2)

print "Clicking the 'back' button"
device.touch (calcWidth(100), calcHeight(90), "DOWN_AND_UP")
MonkeyRunner.sleep(2)


print "Finishing the test sequence" 
