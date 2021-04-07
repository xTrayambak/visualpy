""" VisualPy V1.0.A 
(C) Trayambak Rai, 2021-2022
         error_handling.py
This Python script manages error handling and shows the person who wrote the code any kind of mistake in their code or a building bug.
"""
try:
	import ctypes
	import sys
	import random
	import platform
	import psutil
	from psutil import virtual_memory
except ImportError:
	raise ImportError("Unable to import libraries: Handling.py")

from cpu import cpuinfo
from bridge import runtime_error_free

random_messages = [
	"Hi, I'm VisualPy. My hobby is to crash.",
	"I blame Lucy.",
	"You should try Ren'Py!",
	"REEEEEEEEEEEEEEEEE",
	"could not handle error because no",
	"VisualPy went to brazil!",
	"ur mom green",
	"Crash, debug, repeat",
	"am pro",
	"Roblox Slenders are weird and should not exist, really, I mean it.",
	"Nope, I'm not letting you sleep peacefully thinking you've made progress on your game today! >:)"
]

crash_reason = "Unknown"
available_memory = psutil.virtual_memory().available * 100 / psutil.virtual_memory().total


# os problem #1 - using other operating systems like Linux or MacOS
if sys.platform == "linux" or sys.platform == "macos":
	if sys.platform == "linux":
		crash_reason = "You are using a Linux machine. VisualPy was always tested on Windows and never Linux or any other operating system."
	elif sys.platform == "macos":
		crash_reason = "You are using a machine running MacOS. VisualPy was always tested on Windows and never MacOS or any other operating system."

# error #2 - out of memory - this usually happens when the computer no longer has memory to provide to the Python interpreter
if available_memory <= 0:
	crash_reason = "Your computer ran out of memory to provide to the Python interpreter. Please check that you have atleast 4GB of memory. This might also be caused by an unoptimized game running on an unoptimized version of VisualPy. Too many complex calculations or excessive use of demo RNG features."

# error #3 - logical errors - the person who wrote code for their game wrote it wrong! oh noes!
if runtime_error_free != True:
	crash_reason = "An error occured in the scripts! The interpreter has detected something wrong."

def ThrowError(window_name: str, error: str):
	with open('traceback.txt', 'w') as traceback_log:
		rand = random.choice(random_messages)
		cpu = cpuinfo.cpu.info[0]["ProcessorNameString"]
		ram = virtual_memory()
		ram.total  # total physical memory available
		traceback_log.write(f"## {rand} \n\n\n\nVisualPy encountered an unhandled error.: \n\n\n {error} \n\n ### Debug Information ### \n Architecture: {sys.platform} \n Central Processing Unit Family (CPU): {platform.processor()} \n Central Processing Unit Model (CPU): {cpu} \n Guessed reason of crash: {crash_reason} \n Physical RAM available (total): {ram}")
		traceback_log.close()
	ctypes.windll.user32.MessageBoxW(0, error, window_name, 2)