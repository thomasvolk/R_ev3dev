from R_ev3dev.peripheral import PeripheralCommand, PeripheralAction
from R_ev3dev.ev3 import ev3dev2


class On(PeripheralAction):
    def __init__(self):
        super().__init__("on")

    def invoke(self, context, args):
        in_1 = args[0]
        touch_sensor  = ev3dev2.sensor.lego.TouchSensor(address=in_1)
        context["touch_sensor"] = touch_sensor
        return touch_sensor


class IsPressed(PeripheralAction):
    def __init__(self):
        super().__init__("is_pressed")

    def invoke(self, context, args):
        return context["touch_sensor"].is_pressed


class Touch(PeripheralCommand):
    """ reads the touch sensor

        touch <id> on <in>
        touch <id> is_pressed

    """
    def __init__(self, name):
        super().__init__(name, [
                            On(),
                            IsPressed()
                         ])
