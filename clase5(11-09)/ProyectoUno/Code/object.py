import glm

class Object:
    def __init__(self, position = (0.0,0.0,0.0), rotation = (0.0, 0.0, 0.0), scale = (1.0, 1.0, 1.0)):
        self.position = position
        self.rotation = rotation
        self.scale = scale
    
    @property
    def object_matrix(self):
        #transformaciones: traslacion, rotacion, escala
        m_object = glm.mat4()
        m_object = glm.translate(m_object, self.position)
        m_object = glm.rotate(m_object, self.rotation, glm.vec3(1,1,1))
        m_object = glm.scale(m_object, self.scale)
        return m_object

    def render(self):
        #decirle a la gpu que me renderice
        print ("render")