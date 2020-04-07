from R_ev3dev.peripheral import BackgroundPeripheralCommand, PeripheralAction
from R_ev3dev.ev3 import ev3dev2


class On(PeripheralAction):
    def __init__(self):
        super().__init__("on")

    def invoke(self, context, args):
        out_1 = args[0]
        out_2 = args[1]
        move_tank  = ev3dev2.motor.MoveTank(out_1, out_2)
        context["tank"] = move_tank
        return move_tank


class OnForRotations(PeripheralAction):
    def __init__(self):
        super().__init__("on_for_rotations")

    def invoke(self, context, args):
        left_speed = int(args[0])
        right_speed = int(args[1])
        rotations = float(args[2])
        return context["tank"].on_for_rotations(
            ev3dev2.motor.SpeedPercent(left_speed),
            ev3dev2.motor.SpeedPercent(right_speed),
            rotations
        )


class Tank(BackgroundPeripheralCommand):
    """ controls a pair of motors simultaneously, via individual speed setpoints for each motor

        tank <id> on <out_left> <out_right>
        tank <id> on_for_rotations <left_speed_percent> <right_speed_percent> <rotations>
        tank <id> run_in_background true|false

    """
    def __init__(self, name):
        super().__init__(name, [
                            On(),
                            self.with_background_proxy(OnForRotations())
                         ])
