from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import commands
import sys
import os

# Prerequisites:
# - the main menu screen is displayed
# - there is an active profile
# - level 4 in package 1 is unlocked
# - the zoom buttons are enabled
# This was tested on a device with a display resolution of 1280x720

def addAlligator(x, y):
	print "Dragging an alligator on to the screen"
	device.drag ((calcWidth(1150), calcHeight(140)), (calcWidth(x), calcHeight(y)), 0.5, 50)
	MonkeyRunner.sleep(2)

def addEgg(x, y):
	print "Dragging an egg on to the screen"
	device.drag ((calcWidth(1150), calcHeight(370)), (calcWidth(x), calcHeight(y)), 0.5, 50)
	MonkeyRunner.sleep(2)


def addAgedAlligator(x, y):
	print "Dragging an aged alligator on to the screen"
	device.drag ((calcWidth(1150), calcHeight(240)), (calcWidth(800), calcHeight(90)), 0.5, 50)
	MonkeyRunner.sleep(2)

def colorBoardObject(objectX, objectY, colorX, colorY) :
	print "Clicking the uncollerd board object"
	device.touch (calcWidth(objectX), calcHeight(objectY), "DOWN_AND_UP")
	MonkeyRunner.sleep(2)

	print "Selecting a color"
	device.touch (calcWidth(colorX), calcHeight(colorY), "DOWN_AND_UP")
	MonkeyRunner.sleep(2)


def calcWidth(width):
	return int(int(displayWidth) * int(width) / int(1280))

def calcHeight(height):
	return int(int(displayHeight) * int(height) / int(720))

print "Starting test sequence T160"

device = MonkeyRunner.waitForConnection()

displayWidth = device.getProperty("display.width")
displayHeight = device.getProperty("display.height")


print "Clicking the 'play' button"
device.touch (calcWidth(450), calcHeight(350), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Selecting a level package"
device.touch (calcWidth(400), calcHeight(400), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Selecting the first level"
device.touch (calcWidth(1050), calcHeight(170), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

addEgg(400,150)

addAlligator(400, 150)
colorBoardObject(610, 110, 710, 260)

print "Clicking the 'zoom in' button"
device.drag ((calcWidth(90), calcHeight(510)), (calcWidth(90), calcHeight(510)), 1, 50)
MonkeyRunner.sleep(2)

print "Clicking the 'zoom out' button"
device.drag ((calcWidth(90), calcHeight(630)), (calcWidth(90), calcHeight(630)), 1, 50)
MonkeyRunner.sleep(2)

print "Clicking the 'show end constellation' button"
device.touch (calcWidth(90), calcHeight(380), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Closing the displayed end constellation"
device.touch (calcWidth(90), calcHeight(380), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Clicking the 'ingame menu' button"
device.touch (calcWidth(90), calcHeight(100), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Clicking the 'reset' button"
device.touch (calcWidth(600), calcHeight(190), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

for i in range(3):

	addAlligator(800, 90)
	colorBoardObject(800, 90, 710, 260)

	addEgg(800, 90)
	colorBoardObject(780, 170, 710, 260)

	print "Moving the screen camera"
	device.drag ((calcWidth(900), calcHeight(200)), (calcWidth(700), calcHeight(200)), 1, 50)
	MonkeyRunner.sleep(2)

addAgedAlligator(800, 90)

addEgg(800, 90)
colorBoardObject(765, 150, 710, 450)

addEgg(800, 90), 
colorBoardObject(900, 150, 710, 450)


print "Finishing the test sequence" 


