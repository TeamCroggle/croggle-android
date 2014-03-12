from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import commands
import sys
import os

# Prerequisites:
# - the main menu screen is displayed
# - there is an active profile
# - level 1 in package 2 is unlocked
# This was tested on a device with a display resolution of 1280x720


def calcWidth(width):
	return int(int(displayWidth) * int(width) / int(1280))

def calcHeight(height):
	return int(int(displayHeight) * int(height) / int(720))

print "Starting test sequence T210"

device = MonkeyRunner.waitForConnection()

displayWidth = device.getProperty("display.width")
displayHeight = device.getProperty("display.height")


print "Clicking the 'play' button"
device.touch (calcWidth(450), calcHeight(350), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Moving the screen camera"
device.drag ((calcWidth(1000), calcHeight(200)), (calcWidth(200), calcHeight(200)), 0.1, 50)
MonkeyRunner.sleep(2)

print "Selecting a level package"
device.touch (calcWidth(800), calcHeight(400), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Selecting the first level"
device.touch (calcWidth(340), calcHeight(260), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Clicking the 'play' button"
device.touch (calcWidth(1140), calcHeight(500), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Clicking the 'okay' button"
device.touch (calcWidth(640), calcHeight(520), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Selecting the first answer"
device.touch (calcWidth(300), calcHeight(90), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Moving the screen camera"
device.drag ((calcWidth(1100), calcHeight(300)), (calcWidth(100), calcHeight(300)), 0.5, 50)
MonkeyRunner.sleep(2)

print "Selecting the third answer"
device.touch (calcWidth(960), calcHeight(90), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Clicking the 'play' button"
device.touch (calcWidth(1140), calcHeight(500), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Clicking the 'okay' button"
device.touch (calcWidth(640), calcHeight(520), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Moving the screen camera"
device.drag ((calcWidth(300), calcHeight(300)), (calcWidth(1000), calcHeight(300)), 0.5, 50)
MonkeyRunner.sleep(2)

print "Unselecting the first answer"
device.touch (calcWidth(300), calcHeight(90), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Clicking the 'play' button"
device.touch (calcWidth(1140), calcHeight(500), "DOWN_AND_UP")
MonkeyRunner.sleep(3)

print "Clicking the 'play' button"
device.touch (calcWidth(1140), calcHeight(500), "DOWN_AND_UP")
MonkeyRunner.sleep(20)

print "Clicking the 'main menu' button"
device.touch (calcWidth(960), calcHeight(620), "DOWN_AND_UP")
MonkeyRunner.sleep(2)


print "Finishing the test sequence" 


