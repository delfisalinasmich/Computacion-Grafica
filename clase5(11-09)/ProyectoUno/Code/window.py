import pyglet
import moderngl

class Window(pyglet.window.Window)
    def __init__(self, width, height, title):
        super().__init__(width,height,title, resizable = True)
        self.context = moderngl.create_context()
        self.scene = None

    

    def on_draw(self):
        self.clear()
        self.context.clear(0.1,0.1,0.1) #pueden agregar color de fondo
        if self.scene:
            self.scene.render()


    def run(self):
        pyglet.app.run()