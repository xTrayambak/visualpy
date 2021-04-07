""" VisualPy V1.0.A 
(C) Trayambak Rai, 2021-2022
         error_handling.py
This Python script manages error handling and shows the person who wrote the code any kind of mistake in their code or a building bug.
"""
### import in-built libraries ###

### common libs ###
from pyglet.gl import *
from pyglet.window import key, mouse

class Window(pyglet.window.Window):
	def __init__(self, gameObj,graphicsObjects, *args, **kwargs):
		self.x = gameObj.width
		self.y = gameObj.height
		self.graphicsObjects = graphicsObjects
		super(Window, self).__init__(*args, **kwargs)


	# called by pyglet to draw canvas
	def on_draw(self):
		print("[VisualPy.window]: Refreshed frames at a rate of {}".format(
			int(pyglet.clock.get_fps())
			))
		self.clear()
		self.set_2d()
		for elementObj in self.graphicsObjects:
			elementObj.main.draw()

	def set_2d(self):
		""" Configure OpenGL to draw in 2d.

		"""
		width, height = self.get_size()
		glDisable(GL_DEPTH_TEST)
		viewport = self.get_viewport_size()
		glViewport(0, 0, max(1, viewport[0]), max(1, viewport[1]))
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		glOrtho(0, max(1, width), 0, max(1, height), -1, 1)
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()