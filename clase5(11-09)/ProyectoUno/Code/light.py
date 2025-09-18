import glm

class Light:
    def __init__(self, position = (0.0, 5.0, -10.0), direction = (0.0, 0.0, 0.0), color = (1.0, 1.0, 1.0)):
        self.position = position
        self.color = color
        self.direction = direction
        self.intensity = 1.0

    @property
    def light_matrix(self):
        return glm.lookAt(self.position, self.direction, (0.0, 0.1, 0.0))
