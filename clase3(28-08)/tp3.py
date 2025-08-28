import pyglet # For windowing and user input
import moderngl # For OpenGL context and rendering
import numpy as np # For numerical operations

class Window (pyglet.window.Window): #ventana
    def __init__(self):
        super().__init__(640, 480, "TP3 - Salinas") #ancho por alto y nombre de ventana
        # crear mi canvas ctx = contexto
        self.ctx = moderngl.create_context() #contexto de OpenGL / canvas new canvas de cpu

Window() # crear una instancia de la clase window
pyglet.app.run() #loop de eventos