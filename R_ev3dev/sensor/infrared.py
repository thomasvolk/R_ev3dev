from R_ev3dev.peripheral import PeripheralCommand, PeripheralAction
from R_ev3dev.ev3 import ev3dev2


class On(PeripheralAction):
    def __init__(self):
        super().__init__("on")

    def invoke(self, context, args):
        in_1 = args[0]
        infrared_sensor  = ev3dev2.sensor.lego.InfraredSensor(address=in_1)
        context["infrared_sensor"] = infrared_sensor
        return infrared_sensor


class GetDistance(PeripheralAction):
    def __init__(self):
        super().__init__("distance")

    def invoke(self, context, args):
        channel = args[0]
        return context["infrared_sensor"].distance(channel=channel)


class Infrared(PeripheralCommand):
    def __init__(self, name):
        super().__init__(name, [
                            On(),
                            GetDistance()
                         ])
