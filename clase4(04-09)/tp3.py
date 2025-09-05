import pyglet # For windowing and user input
import moderngl # For OpenGL context and rendering
import numpy as np # For numerical operations
from pathlib import Path # For file path management
import time

class Window (pyglet.window.Window): #ventana
    def __init__(self):
        super().__init__(800, 600, "TP3 - Salinas - Multiplication Tables Mandalas") #ancho por alto y nombre de ventana
        # crear mi canvas ctx = contexto
        self.ctx = moderngl.create_context() #contexto de OpenGL / canvas new canvas de cpu
        
        self.start_time = time.time()
        self.mouse_x = 0.0
        self.mouse_y = 0.0
        self.mouse_pressed = False
        
        shader_dir = Path(__file__).parent / "shaders" #ruta de los shaders
        with open(shader_dir / "vertex.glsl") as f:
            vertex_shader_source = f.read()
        with open(shader_dir / "fragment.glsl") as f:
            fragment_shader_source = f.read()
        self.prog = self.ctx.program(vertex_shader=vertex_shader_source, fragment_shader=fragment_shader_source)
        
        quad_points = [
            (-1.0, -1.0),   # abajo izquierda
            (1.0, -1.0),    # abajo derecha
            (-1.0, 1.0),    # arriba izquierda
            (1.0, 1.0)      # arriba derecha
        ] # 4 vertices array de puntos x, y
        
        vertices = []
        for (px, py) in quad_points:
            vertices.extend([px, py]) # solo posición, sin color
        
        vertices_array = np.array(vertices, dtype='f4') #float32
        vbo = self.ctx.buffer(vertices_array.tobytes()) #tobytes convierte el array en bytes
        
        self.vao = self.ctx.vertex_array(
            self.prog,
            [(vbo, '2f', 'in_pos')]
        ) #dato de la figura

    def on_mouse_motion(self, x, y, dx, dy):
        self.mouse_x = float(x)
        self.mouse_y = float(y)
    
    def on_mouse_press(self, x, y, button, modifiers):
        self.mouse_pressed = True
        self.mouse_x = float(x)
        self.mouse_y = float(y)
    
    def on_mouse_release(self, x, y, button, modifiers):
        self.mouse_pressed = False

    def on_draw(self):
        self.clear()
        self.ctx.clear(0.0, 0.0, 0.0) #renderiza la figura
        
        current_time = time.time() - self.start_time
        
        # Configurar uniformes
        if 'iTime' in self.prog:
            self.prog['iTime'].value = current_time
        if 'iResolution' in self.prog:
            self.prog['iResolution'].value = (float(self.width), float(self.height))
        if 'iMouse' in self.prog:
            mouse_z = 1.0 if self.mouse_pressed else 0.0
            self.prog['iMouse'].value = (self.mouse_x, self.mouse_y, mouse_z, 0.0)
        
        self.vao.render(mode = moderngl.TRIANGLE_STRIP) #renderiza la figura

Window() # crear una instancia de la clase window
pyglet.app.run() #loop de eventos
