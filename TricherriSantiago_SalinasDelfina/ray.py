import glm 

class Ray:
    def __init__(self, origin = (0,0,0), direction = (0,0,1)):
        self.__origin = glm.vec3(*origin)
        self.__direction = glm.normalize(glm.vec3(*direction))

    def point_at_parameter(self, t: float) -> glm.vec3:
        return self.__origin + t * self.__direction
    
    #Encapsulamiento
    @property
    def origin(self) -> glm.vec3:
        return self.__origin

    @property
    def direction(self) -> glm.vec3:
        return self.__direction
