from R_ev3dev.peripheral import PeripheralCommand, PeripheralAction
from R_ev3dev.ev3 import ev3dev2


class On(PeripheralAction):
    def __init__(self):
        super().__init__("on")

    def invoke(self, context, args):
        out = args[0]
        motor = ev3dev2.motor.MediumMotor(out)
        context["medium_motor"] = motor
        return motor


class OnForRotations(PeripheralAction):
    def __init__(self):
        super().__init__("on_for_rotations")

    def invoke(self, context, args):
        speed = int(args[0])
        rotations = float(args[1])
        return context["medium_motor"].on_for_rotations(
            ev3dev2.motor.SpeedPercent(speed),
            rotations
        )


class MediumMotor(PeripheralCommand):
    def __init__(self, name):
        super().__init__(name, [
                            On(),
                            OnForRotations()
                         ])
