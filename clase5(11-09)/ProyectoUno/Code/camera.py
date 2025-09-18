import glm

class Camera:
    def __init__(self, position = (0.0, 0.0, -10.0), target = (0.0,0.0,0.0)):
        self.position = position
        self.target = target
        self.up = (0.0, 1.0, 0.0)

    @property
    def view_matrix(self):
        return glm.lookAt(self.position, self.target, self.up)
    
    @property
    def projection_matrix(self):
        return glm.perspective(glm.radians(45, 16/9, 0.1, 100))
    
