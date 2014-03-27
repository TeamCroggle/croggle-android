from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import commands
import sys
import os

# Prerequisites:
# - the app is in the 5th level of the first level package
# - an alligator(colored in any color) with another alligator(also colored. in a different color) beneath it with an egg beneath it was added to the board
# - the zoom buttons are enabled

# This was tested on a device with a display resolution of 1280x720
# Sometimes an error appears while running a test case for the first time, restarting it usually solves this problem

def calcWidth(width):
	return int(int(displayWidth) * int(width) / int(1024))

def calcHeight(height):
	return int(int(displayHeight) * int(height) / int(552))

print "Starting coverage sequence 01"


device = MonkeyRunner.waitForConnection()

displayWidth = device.getProperty("display.width")
displayHeight = device.getProperty("display.height")

print displayWidth
print displayHeight

print "Clicking the 'menu' button"
device.touch (calcWidth(80), calcHeight(80), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Clicking the 'resume' option in the menu"
device.touch (calcWidth(512), calcHeight(74), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "start Simulation mode"
device.touch (calcWidth(900), calcHeight(400), "DOWN_AND_UP")
MonkeyRunner.sleep(1)

print "Clicking the 'menu' button (in Simulation mode)"
device.touch (calcWidth(80), calcHeight(80), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Clicking the 'resume' option in the menu(in Simulation mode)"
device.touch (calcWidth(512), calcHeight(74), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Clicking the 'zoom +' button (in Simulation mode)"
device.touch (calcWidth(60), calcHeight(403), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Clicking the 'zoom -' button(in Simulation mode)"
device.drag ((calcWidth(60), calcHeight(490)), (calcWidth(60), calcHeight(490)), 1, 50)
MonkeyRunner.sleep(2)

print "Clicking the 'zoom +' button(in Simulation mode)"
device.drag ((calcWidth(60), calcHeight(403)), (calcWidth(60), calcHeight(403)), 1, 50)
MonkeyRunner.sleep(2)

print "Clicking the 'zoom -' button(in Simulation mode)"
device.touch (calcWidth(60), calcHeight(490), "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Clicking the 'zoom -' button(in Simulation mode)"
device.touch (calcWidth(60), calcHeight(490), "DOWN_AND_UP")
MonkeyRunner.sleep(2)


print "start Simulation"
device.touch (calcWidth(900), calcHeight(400), "DOWN_AND_UP")
MonkeyRunner.sleep(1)

print "change simulation speed mode"
device.drag ((calcWidth(650), calcHeight(486)), (calcWidth(600), calcHeight(486))) #careful here without calcHeight!!!!
MonkeyRunner.sleep(2)

