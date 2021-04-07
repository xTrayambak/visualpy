""" VisualPy V1.0.A 
(C) Trayambak Rai, 2021-2022
         mouse_control.py
This Python Script allows the person who wrote a program to control/hijack the player's mouse with no or less effort. Similar to Ren'Py's mouse control functions.
"""
try:
	import pyautogui
	import time
	import keyboard
except ImportError:
	Exception("ImportError: pyautogui not found! It is required to use a few elements of VisualPy!")

class MouseControls:
	def TweenMouseToPos(pos_x: int, pos_y: int, time: int):
		print("TweenMouseToPos() is being used.")
		pyautogui.moveTo(pos_x, pos_y, time, pyautogui.easeInQuad)

	def Click(x: int, y: int, button: str):
		print("Click() is being used.")
		pyautogui.click(x=x, y=y, button=button)

	def GetMousePosition():
		x, y = pyautogui.position()
		return x, y
