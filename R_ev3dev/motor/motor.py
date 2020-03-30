from R_ev3dev.peripheral import PeripheralCommand, PeripheralAction
from R_ev3dev.interpreter import Command
from R_ev3dev.ev3 import ev3dev2


class ListMotors(Command):
    """ list all motors """
    def invoke(self, interpreter_context, args):
        return [{'driver_name': m.driver_name, 'address': m.address} for m in ev3dev2.motor.list_motors()]


class On(PeripheralAction):
    def __init__(self, motor_type_factory):
        self.__motor_type_factory = motor_type_factory
        super().__init__("on")

    def invoke(self, context, args):
        out = args[0]
        motor = self.__motor_type_factory(out)
        context["motor"] = motor
        return motor


class OnForRotations(PeripheralAction):
    def __init__(self):
        super().__init__("on_for_rotations")

    def invoke(self, context, args):
        speed = int(args[0])
        rotations = float(args[1])
        return context["motor"].on_for_rotations(
            ev3dev2.motor.SpeedPercent(speed),
            rotations
        )


class Motor(PeripheralCommand):
    def __init__(self, name, motor_type_factory):
        super().__init__(name, [
                            On(motor_type_factory),
                            OnForRotations()
                         ])


class LargeMotor(Motor):
    """ controls a large motor

        large_motor <id> on <out>
        large_motor <id> on_for_rotations <speed_percent> <rotations>

    """
    def __init__(self, name):
        super().__init__(name, lambda out: ev3dev2.motor.LargeMotor(out))


class MediumMotor(Motor):
    """ controls a medium motor

        medium_motor <id> on <out>
        medium_motor <id> on_for_rotations <speed_percent> <rotations>

    """
    def __init__(self, name):
        super().__init__(name, lambda out: ev3dev2.motor.MediumMotor(out))
