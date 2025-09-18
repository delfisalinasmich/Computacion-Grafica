from Code.window import Window
from Code.scene import Scene

if __name__ == "__main__":
    #crear ventana
    window = Window(1280, 720, "Graphic Engine")
    #cargar una escena en esa ventana
    window.set_scene(Scene())
    #ejecutar el loop de vida de la ventana
    window.run()