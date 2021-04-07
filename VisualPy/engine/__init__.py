import pyglet
from window import Window
from logic import Sprite
from logic import Image

class Logger:
    def __init__(self):
        self.history = []
        self.info = {'errors': 0, 'warnings': 0}

    def log(self, msg, isErr=False, isWarnings=False):
        """
        Description:\n
        Logs a message `msg` to the console. Parameters bool `isErr` and bool `isWarnings` define if this is an error or a warning. Errors pause the game.
        --------
        Parameters:\n
        `msg` - The message to output\n
        `isErr` - If it is an error\n
        `isWarnings` - If it is a warning\n
        """

        self.history.append(object=f'[VisualPy.Engine.Logger]: {str(msg)}')
        if isErr == True:
            self.info['errors']+=1
        if isWarnings == True:
            self.info['warnings']+=1
        print(f"[VisualPy.Engine.Logger]: {str(msg)}")
        


    def LogError(self, err):
        """
        Log an error to the console.
        """
        self.log(msg=tostring(err), isErr=True)

class gameProfile():
    def __init__(self, res):
        self.width, self.height = res

class Game(object):
    def __init__(self, caption, resolution, objects, vsync=False):
        self.name = caption
        self.vsync = vsync
        self.objects = objects
        self.profile = gameProfile(resolution)

        self.window = Window(gameObj=self.profile, graphicsObjects=self.objects, caption=self.name, vsync=self.vsync)

    def style(a: int):
        """
        Change the style the window's title is rendered.

        Parameters:
        `a` - 1 will make a window with the caption "{Your Game Name Here} | {Framerate}"
        """
        raise NotImplementedError

    def caption(caption: str):
        self.name = caption
        self.window.set_caption(self.name)

    def add_obj(self, obj):
        """
        In order to render a new object, it must be added using this method.
        """
        self.objects.append(obj)

    def exit(reason=None):
        with open('debug.log', 'w') as log:
            if reason != None:
                log.write(f'[VisualPy.Game]: Class terminated because of {reason}.')
            elif reason == None:
                log.write(f'[VisualPy.Game]: Class terminated with no reason provided.')

        self.window.close()

    def gfx_init():
        raise NotImplementedError

    def run(a):
        pyglet.app.run()

    def unpack_res(tupleTar):
        width, height = tupleTar
        return width, height