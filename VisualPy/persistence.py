""" VisualPy V1.0.A 
(C) Trayambak Rai, 2021-2022
         persistence.py
This Python script manages screenshot data and savedata.
"""

from engine import Handling

try:
	import os
	import json
	import sys
	import jsonpickle
	import base64
except ImportError:
	error_handling.ErrorHandling.ThrowError("ModuleNotFoundError", "VisualPy encountered a ModuleNotFoundError while importing a few libraries. Your game will not work till all the libraries required are installed.")
except ModuleNotFoundError:
	error_handling.ErrorHandling.ThrowError("ModuleNotFoundError", "VisualPy encountered a ModuleNotFoundError while importing a few libraries. Your game will not work till all the libraries required are installed.")


## this is the structure of a .visualpy file
"""
savedata[current dialog here, profile]
"""

class Savedata():

	def __init__(self, profile: int, current_dialog: int):
		self.current_dialog = current_dialog
		self.profile = profile

	def Save(self):
		data = {
			"current_dialog": str(self.current_dialog),
			"profile": str(self.profile)
		}
		json_encode = json.dumps(data, indent = 4)
		with open(f'savefile_{self.profile}.vsave', 'w') as dat:
			a = jsonpickle.encode(data)
			dat.write(a)

		print(a)
		print("Save was saved to file. B64:")
		print("Saved to .visualpy file successfuly.")

	def Load(profile: int):
		try:
			with open(f"savefile_{profile}.vsave", "r") as savefile:
				savedata_message = savefile.read()
				savedata_bytes = savedata_message.encode('ascii')
				savedata_b = base64.b64decode(savedata_bytes)
				savedata = savedata_b.decode('ascii')
				print(savedata)
				savedata_converted = json.loads(savedata)
				save_table = []
				save_table.append(int(savedata_converted["current_dialog"]))
				save_table.append(int(savedata_converted["profile"]))
				print(f"VisualPy: Savedata profile {profile} loaded successfuly!")
				print(save_table)
				return save_table
		except FileNotFoundError:
			print(f"No such savedata named savedata_{profile} was found.")
			return None