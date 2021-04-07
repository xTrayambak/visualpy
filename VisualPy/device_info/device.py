""" VisualPy V1.0.A 
(C) Trayambak Rai, 2021-2022
         device.py
This Python script manages operating system info.
"""

try:
	import sys
except ImportError:
	Exception("ImportError: VisualPy failed to load 'sys' library for device.py!")

class DeviceInfo:
	device = sys.platform

	def GetRawPlatform():
		return sys.platform
	def GetPrecisePlatform():
		if sys.platform == "win32":
			return "win32bit"
		elif sys.platform == "win64":
			return "win64bit"
		elif sys.platform == "macos":
			return "macos"
		else:
			Exception("Unable to determine OS!")
			return None

	def GetPlatform():
		if sys.platform == "win32" or "win64":
			return "Windows"
		elif sys.platform == "macos":
			return "MacOS"
		elif sys.platform == "linux":
			return "Linux"