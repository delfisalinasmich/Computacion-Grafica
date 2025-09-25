from window import Window
from shader_program import ShaderProgram
from cube import Cube
from camera import Camera
from scene import Scene

import os

# --- Loop principal ---
window = Window(800, 600, "Basic Graphic Engine")

# Obtener ruta absoluta a los shaders
shader_dir = os.path.join(os.path.dirname(__file__), '..', 'shaders')
vertex_shader_path = os.path.join(shader_dir, 'basic.vert')
fragment_shader_path = os.path.join(shader_dir, 'basic.frag')

shader_program = ShaderProgram(window.ctx, vertex_shader_path, fragment_shader_path)
cube1 = Cube((-2, 0, 0), (0, 45, 0), (1, 1, 1), name="Cube1")
cube2 = Cube((2, 0, 0), (0, 45, 0), (1, 0.5, 1), name="Cube2")
camera = Camera((0, 0, 6), (0, 0, 0), (0, 1, 0), 45, window.width / window.height, 0.1, 100.0)
scene = Scene(window.ctx, camera)
scene.add_object(cube1, shader_program)
scene.add_object(cube2, shader_program)
window.set_scene(scene)

window.run()