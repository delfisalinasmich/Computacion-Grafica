from window import Window
from texture import Texture
from material import Material
from shader_program import ShaderProgram
from cube import Cube
from quad import Quad
from camera import Camera
from scene import Scene
import numpy as np
import os

# --- Loop principal ---

window = Window(800, 600, "Basic Graphic Engine")

# Obtener ruta absoluta a los shaders
shader_dir = os.path.join(os.path.dirname(__file__), '..', 'shaders')
vertex_shader_path = os.path.join(shader_dir, 'basic.vert')
fragment_shader_path = os.path.join(shader_dir, 'basic.frag')
vertex_shader_sprite = os.path.join(shader_dir, 'sprite.vert')
fragment_shader_sprite = os.path.join(shader_dir, 'sprite.frag')

shader_program = ShaderProgram(window.ctx, vertex_shader_path, fragment_shader_path)
shader_program_skybox = ShaderProgram(window.ctx, vertex_shader_sprite, fragment_shader_sprite)

skybox_texture = Texture(image_data= np.array([120, 175, 195, 255], dtype='uint8'))

material = Material(shader_program)
material_sprite = Material(shader_program_skybox, textures_data = [skybox_texture])

cube1 = Cube((-2, 0, 2), (0, 45, 0), (1, 1, 1), name="Cube1")
cube2 = Cube((2, 0, 2), (0, 45, 0), (1, 0.5, 1), name="Cube2")
quad = Quad((0,0,0), (0,0,0), (6,5,1), name="Sprite")

camera = Camera((0, 0, 10), (0, 0, 0), (0, 1, 0), 45, window.width / window.height, 0.1, 100.0)

scene = Scene(window.ctx, camera)

scene.add_object(quad, material_sprite)
scene.add_object(cube1, material)
scene.add_object(cube2, material)
window.set_scene(scene)

window.run()