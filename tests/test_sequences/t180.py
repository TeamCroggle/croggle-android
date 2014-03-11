from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import commands
import sys
import os

# Prerequisites:
# - the main menu screen is displayed
# - there are more than two profiles stored
# This was tested on a device with a display resolution of 1280x720

def calcWidth(width):
	return int(int(displayWidth) * int(width) / int(1280))

def calcHeight(height):
	return int(int(displayHeight) * int(height) / int(720))

print "Starting test sequence T180"

device = MonkeyRunner.waitForConnection()

displayWidth = device.getProperty("display.width")
displayHeight = device.getProperty("display.height")

print "Clicking the 'statistic' button"
device.touch (calcWidth(250) , calcHeight(620), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Opening the 'select profile' drop down"
device.touch (calcWidth(900), calcHeight(100), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Secting a profile"
device.touch (calcWidth(900), calcHeight(210), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Selecting the category 'actions'"
device.touch (calcWidth(650), calcHeight(210), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Opening the 'select profile' drop down"
device.touch (calcWidth(900), calcHeight(100), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Secting a profile"
device.touch (calcWidth(900), calcHeight(150), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Selecting the category 'game'"
device.touch (calcWidth(1000), calcHeight(210), "DOWN_AND_UP")
MonkeyRunner.sleep(2)





print "Finishing the test sequence" 
