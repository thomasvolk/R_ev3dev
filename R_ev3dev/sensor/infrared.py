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
        sensor = context["infrared_sensor"]
        if len(args):
            channel = args[0]
            return sensor.distance(channel=channel)
        else:
            return sensor.distance()


class Infrared(PeripheralCommand):
    """ reads the infrared sensor

        infrared <id> on <in>
        infrared <id> distance [<channel>]

    """
    def __init__(self, name):
        super().__init__(name, [
                            On(),
                            GetDistance()
                         ])
