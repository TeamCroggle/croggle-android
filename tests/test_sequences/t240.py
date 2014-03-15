
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import commands
import sys
import os

# Prerequisites:
# none
# This was tested on a device with a display resolution of 1280x720

def calcWidth(width):
	return int(int(displayWidth) * int(width) / int(1280))

def calcHeight(height):
	return int(int(displayHeight) * int(height) / int(720))

print "Starting test sequence T240"

device = MonkeyRunner.waitForConnection()

print "Installing the apk"
device.installPackage('../../bin/croggle-android.apk')
runComponent = 'de.croggle' + '/' + 'de.croggle.MainActivity'

print "Starting the app"
device.startActivity(component=runComponent)
MonkeyRunner.sleep(18)

displayWidth = device.getProperty("display.width")
displayHeight = device.getProperty("display.height")

print "Clicking the android back button"
device.press('KEYCODE_BACK', "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "Clicking the 'ok' button"
device.touch(calcWidth(450), calcHeight(520), "DOWN_AND_UP")
MonkeyRunner.sleep(2)



