from R_ev3dev.peripheral import PeripheralCommand, PeripheralAction
from R_ev3dev.ev3 import ev3dev2


class On(PeripheralAction):
    def __init__(self):
        super().__init__("on")

    def invoke(self, context, args):
        in_1 = args[0]
        gyro_sensor  = ev3dev2.sensor.lego.GyroSensor(address=in_1)
        context["gyro_sensor"] = gyro_sensor
        return gyro_sensor


class Angle(PeripheralAction):
    def __init__(self):
        super().__init__("angle")

    def invoke(self, context, args):
        return context["gyro_sensor"].angle


class Gyro(PeripheralCommand):
    """ reads the gyro sensor

        gyro <id> on <in>
        gyro <id> angle

    """
    def __init__(self, name):
        super().__init__(name, [
                            On(),
                            Angle()
                         ])
