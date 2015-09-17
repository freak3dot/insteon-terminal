#-------------------------------------------------------------------------------
#
# Base class for all dimmers
#
import commands
import message

from us.pfrommer.insteon.cmd.msg import InsteonAddress
from device import Device

class Dimmer(Device):
	def __init__(self, name, adr):
		Device.__init__(self, name, adr)

	def on(self, level=0xFF):
		commands.writeMsg(message.createStdMsg(
			InsteonAddress(self.getAddress()), 0x0F, 0x11, level, -1))

	def onFast(self, level=0xFF):
		commands.writeMsg(message.createStdMsg(
			InsteonAddress(self.getAddress()), 0x0F, 0x12, level, -1))

	def off(self):
		commands.writeMsg(message.createStdMsg(
			InsteonAddress(self.getAddress()), 0x0F, 0x13, 0x00, -1))

	def offFast(self):
		commands.writeMsg(message.createStdMsg(
			InsteonAddress(self.getAddress()), 0x0F, 0x14, 0x00, -1))

	def incrementalBright(self):
		commands.writeMsg(message.createStdMsg(
			InsteonAddress(self.getAddress()), 0x0F, 0x15, 0x00, -1))

	def incrementalDim(self):
		commands.writeMsg(message.createStdMsg(
			InsteonAddress(self.getAddress()), 0x0F, 0x16, 0x00, -1))

	def startManualChangeUp(self):
		commands.writeMsg(message.createStdMsg(
			InsteonAddress(self.getAddress()), 0x0F, 0x17, 0x01, -1))

	def startManualChangeDown(self):
		commands.writeMsg(message.createStdMsg(
			InsteonAddress(self.getAddress()), 0x0F, 0x17, 0x00, -1))

	def stopManualChange(self):
		commands.writeMsg(message.createStdMsg(
			InsteonAddress(self.getAddress()), 0x0F, 0x18, 0x00, -1))
