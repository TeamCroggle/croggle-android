from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import commands
import sys
import os

# Prerequisites:
# - the main menu screen is displayed
# - there is exactly one profile stored and its name is not 'tom'
# This was tested on a device with a display resolution of 1280x720

def calcWidth(width):
	return int(int(displayWidth) * int(width) / int(1280))

def calcHeight(height):
	return int(int(displayHeight) * int(height) / int(720))

print "Starting test sequence T110"


device = MonkeyRunner.waitForConnection()

displayWidth = device.getProperty("display.width")
displayHeight = device.getProperty("display.height")


print "Clicking the 'user' button"
device.touch (calcWidth(1050), calcHeight(430), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Clicking the plus symobol"
device.touch (calcWidth(600), calcHeight(430), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Clicking the text field"
device.touch (calcWidth(600), calcHeight(310), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Pressing the letter t"
device.touch (calcWidth(575), calcHeight(450), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Pressing the letter o"
device.touch (calcWidth(1070), calcHeight(450), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Pressing the letter m"
device.touch (calcWidth(1020), calcHeight(590), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Closing on-screen keyboard"
device.touch (calcWidth(1210), calcHeight(670), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Clicking the 'next' button"
device.touch (calcWidth(960), calcHeight(470), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Selecting the red alligator"
device.touch (calcWidth(800), calcHeight(400), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Clicking the 'next' button"
device.touch (calcWidth(960), calcHeight(470), "DOWN_AND_UP")
MonkeyRunner.sleep(2)


print "Finishing the test sequence"
