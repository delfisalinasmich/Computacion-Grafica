from Code.camera import Camera
from Code.light import Light

class Scene:
    def __init__(self):
        self.objects = []
        self.camera = None #si queremos muchas camras va lista
        self.light = None
        self.initial_time = 0
    
    def create_camera(self):
        self.camera = Camera()

    def create_light(self):
        self.light = Light()

    def add_object(self, object):
        self.objects.append(object)

    def render(self, context):
        for object in self.objects:
            object.render()
