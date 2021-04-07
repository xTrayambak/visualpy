"""
DialogList
"""
from ErrorTypes import *
from bridge import runtime_error_free
from Handling import *
import pyglet
import random

def remove_spaces(words):
	result = ''
	for w in words:
		if w != ' ':
			result += w

	return result


"""
Sprite data
"""

class Sprite():
	def __init__(self, x, y, textures):
		self.x = x
		self.y = y
		self.textures = textures
		self.texture = self.textures[0] # can be used as idle
		self.main = pyglet.sprite.Sprite(self.texture, self.x, self.y)

	def remove(self):
		"""
		Removes sprite from scene.
		"""
		self.main._unload() # remove the sprite from VRAM in order to maintain efficiency

	def reset(self):
		"""
		Resets sprite position and texture.
		"""
		self.main._unload() # unloads the current sprite

		# reset position
		self.x = 0
		self.y = 0

		# reset texture
		self.texture = self.textures[0]
		self.sprite = pyglet.sprite.Sprite(self.texture.main, self.x, self.y)

	def pose(self, index):
		try:
			self.texture = self.textures[int(index)]
		except IndexError as e:
			raise InvalidArgument("{}: IndexError: No valid texture at {}".format(e, int(index)))



	def _unload(self):
		"""
		Unload sprite from video memory. You should call this function every time you're hiding a sprite for a long time, in order to maintain efficiency. Calling this too many times leads to excessive IO calls.
		"""
		self.main.delete()

class Image():
	def __init__(self, path):
		"""
		Base class for image for sprites.
		"""
		self.path = path
		self.main = pyglet.media.load(self.path)