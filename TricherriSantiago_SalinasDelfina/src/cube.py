import glm
import numpy as np
from hit import HitBoxOBB

class Cube:
    def __init__(self, position=(0,0,0), rotation=(0,0,0), scale=(1,1,1), name="cube"):
        self.name = name
        self.position = glm.vec3(*position)
        self.rotation = glm.vec3(*rotation)
        self.scale = glm.vec3(*scale)
        self.__colision = HitBoxOBB(get_model_matrix=lambda: self.get_model_matrix())

        # Vértices y colores del cubo
        self.vertices = np.array([
            # x, y, z,   r, g, b
            -1, -1, -1,  1, 0, 0,
             1, -1, -1,  0, 1, 0,
             1,  1, -1,  0, 0, 1,
            -1,  1, -1,  1, 1, 0,
            -1, -1,  1,  1, 0, 1,
             1, -1,  1,  0, 1, 1,
             1,  1,  1,  1, 1, 1,
            -1,  1,  1,  0, 0, 0,
        ], dtype='f4')

        self.indices = np.array([
            0, 1, 2, 2, 3, 0,  # cara trasera
            4, 5, 6, 6, 7, 4,  # cara delantera
            0, 4, 7, 7, 3, 0,  # cara izquierda
            1, 5, 6, 6, 2, 1,  # cara derecha
            3, 2, 6, 6, 7, 3,  # cara superior
            0, 1, 5, 5, 4, 0,  # cara inferior
        ], dtype='i4')

    def check_hit(self, origin, direction):
        return self.__colision.check_hit(origin, direction)

    def get_model_matrix(self):
        model = glm.mat4(1)
        model = glm.translate(model, self.position)
        model = glm.rotate(model, glm.radians(self.rotation.x), glm.vec3(1, 0, 0))
        model = glm.rotate(model, glm.radians(self.rotation.y), glm.vec3(0, 1, 0))
        model = glm.rotate(model, glm.radians(self.rotation.z), glm.vec3(0, 0, 1))
        model = glm.scale(model, self.scale)
        return model