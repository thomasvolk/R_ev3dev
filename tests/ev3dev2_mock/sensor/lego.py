

class ColorSensor(object):
    def __init__(self, **kwargs):
        self.color = 0
        self.kwargs = kwargs


class InfraredSensor(object):
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def distance(self, channel=1):
        return 45
