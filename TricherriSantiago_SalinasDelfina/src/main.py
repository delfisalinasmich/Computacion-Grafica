from TricherriSantiago_SalinasDelfina.src.window import Window
from TricherriSantiago_SalinasDelfina.src.shader_program import ShaderProgram
from TricherriSantiago_SalinasDelfina.src.cube import Cube
from TricherriSantiago_SalinasDelfina.src.camera import Camera
from TricherriSantiago_SalinasDelfina.src.scene import Scene

# --- Loop principal ---
window = Window(800, 600, "Basic Graphic Engine")
shader_program = ShaderProgram(window.ctx, 'shaders/basic.vert', 'shaders/basic.frag')
cube1 = Cube((-2, 0, 0), (0, 45, 0), (1, 1, 1), name="Cube1")
cube2 = Cube((2, 0, 0), (0, 45, 0), (1, 0.5, 1), name="Cube2")
camera = Camera((0, 0, 6), (0, 0, 0), (0, 1, 0), 45, window.width / window.height, 0.1, 100.0)
scene = Scene(window.ctx, camera)
scene.add_object(cube1, shader_program)
scene.add_object(cube2, shader_program)
window.set_scene(scene)

window.run()