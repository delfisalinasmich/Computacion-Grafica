import pyglet # For windowing and user input
import moderngl # For OpenGL context and rendering
import numpy as np # For numerical operations

class Window (pyglet.window.Window): #ventana
    def __init__(self):
        super().__init__(640, 480, "TP3 - Salinas") #ancho por alto y nombre de ventana
        # crear mi canvas ctx = contexto
        self.ctx = moderngl.create_context() #contexto de OpenGL / canvas new canvas de cpu
        # primero definimos una figura, porque esto es por cada figura
        quad_points = [(-0.5, 0.5), (0.5, 0.5), (0.5, -0.5), (-0.5, -0.5)] # 4 vertices array de puntos x, y
        # ahora lo que hacemos es: al quad me falta decirle los colores
        vertices = []
        for (px, py) in quad_points:
            r, g, b = 1.0, 1.0, 1.0 # Color rojo
            vertices.extend([px, py, r, g, b]) # guardo por cada pixel un color
        # ahora necesito guardar eso en memoria y la memoria para hacerlo necesito transformar el array en bytes
        vertices_array = np.array(vertices, dtype='f4') #float32
        # dato a guardar en memoria: crear el VBO Vertex Buffer Object
        vbo = self.ctx.buffer(vertices_array.tobytes()) #tobytes convierte el array en bytes
        # una instruccion de como esta guardando ese dato: crear el VAO Vertex Array Object
        self.vao = self.ctx.vertex_array(shader, [vbo, '2f 3f', 'in_pos',  'in_color']) #dato de la figura

Window() # crear una instancia de la clase window
pyglet.app.run() #loop de eventos


