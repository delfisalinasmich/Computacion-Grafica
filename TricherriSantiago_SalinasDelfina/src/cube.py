from hit import HitBox, HitBoxOBB
import numpy as np
import glm

class Cube:
    def __init__(self, position=(0,0,0), rotation=(0,0,0), scale=(1,1,1), name="cube"):
        self.name = name
        self.position = glm.vec3(*position)
        self.rotation = glm.vec3(*rotation)
        self.scale = glm.vec3(*scale)
        self.__colision = HitBoxOBB(get_model_matrix=lambda: self.get_model_matrix())

        # Agrega los vértices y los índices de un cubo
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