from R_ev3dev.peripheral import PeripheralCommand, PeripheralAction
from R_ev3dev.ev3 import ev3dev2


class On(PeripheralAction):
    def __init__(self):
        super().__init__("on")

    def invoke(self, context, args):
        in_1 = args[0]
        color_sensor  = ev3dev2.sensor.lego.ColorSensor(address=in_1)
        context["color_sensor"] = color_sensor
        return color_sensor


class GetColor(PeripheralAction):
    def __init__(self):
        super().__init__("color")

    def invoke(self, context, args):
        return context["color_sensor"].color


class Color(PeripheralCommand):
    def __init__(self, name):
        super().__init__(name, [
                            On(),
                            GetColor()
                         ])
