import numpy as np
import glm

class Sphere:
    def __init__(self, position=(0,0,0), rotation=(0,0,0), scale=(1,1,1), name="sphere", segments=24, rings=16):
        self.name = name
        self.position = glm.vec3(*position)
        self.rotation = glm.vec3(*rotation)
        self.scale = glm.vec3(*scale)

        vertices = []
        indices = []

        # Generar vértices
        for ring in range(rings + 1):
            phi = np.pi * ring / rings
            for seg in range(segments + 1):
                theta = 2 * np.pi * seg / segments
                x = np.sin(phi) * np.cos(theta)
                y = np.cos(phi)
                z = np.sin(phi) * np.sin(theta)
                # Color simple basado en posición
                r = abs(x)
                g = abs(y)
                b = abs(z)
                vertices.extend([x, y, z, r, g, b])

        # Generar índices
        for ring in range(rings):
            for seg in range(segments):
                a = ring * (segments + 1) + seg
                b = a + segments + 1
                indices.extend([a, b, a + 1])
                indices.extend([b, b + 1, a + 1])

        self.vertices = np.array(vertices, dtype='f4')
        self.indices = np.array(indices, dtype='i4')

    def get_model_matrix(self):
        model = glm.mat4(1)
        model = glm.translate(model, self.position)
        model = glm.rotate(model, glm.radians(self.rotation.x), glm.vec3(1, 0, 0))
        model = glm.rotate(model, glm.radians(self.rotation.y), glm.vec3(0, 1, 0))
        model = glm.rotate(model, glm.radians(self.rotation.z), glm.vec3(0, 0, 1))
        model = glm.scale(model, self.scale)
        return model