

class Sensor(object):
    def __init__(self, address=None, **kwargs):
        self.address = address
        self.kwargs = kwargs


class ColorSensor(Sensor):
    def __init__(self, **kwargs):
        self.color = 0
        self.kwargs = kwargs
