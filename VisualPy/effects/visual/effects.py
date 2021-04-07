""" VisualPy V1.0.A 
(C) Trayambak Rai, 2021-2022
         effects.py
This Python Script allows to make certain visual effects.
"""

try:
	import pyautogui
	from visualpy import persistence
except ImportError:
	Exception("ImportError: An error occured in starting VisualPy effects.py! Please send traceback.txt's data to the support discord")

class Effects:
	def screen_tear():
		pyautogui.screenshot()