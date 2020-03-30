OUTPUT_A = 'outA'
OUTPUT_B = 'outB'
OUTPUT_C = 'outC'
OUTPUT_D = 'outD'


class Motor(object):
    def __init__(self, address=None, driver_name=None, **kwargs):
        self.address = address
        self.driver_name = driver_name
        self.kwargs = kwargs
        self.log = []

    def on_for_rotations(self, speed, rotations, brake=True, block=True):
        self.log.append(('on_for_rotations', repr(speed), rotations))


def list_motors():
    return iter([
        Motor(OUTPUT_A, 'lego-ev3-m-motor'),
        Motor(OUTPUT_B, 'lego-ev3-l-motor'),
        Motor(OUTPUT_C, 'lego-ev3-l-motor'),
    ])


class LargeMotor(Motor):
    pass


class MediumMotor(Motor):
    pass


class SpeedPercent(object):
    def __init__(self, percent):
        self.percent = percent

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, self.percent)


class MoveTank(object):
    def __init__(self, left_motor_port, right_motor_port, **kwargs):
        self.left_motor_port = left_motor_port
        self.right_motor_port = right_motor_port
        self.kwargs = kwargs
        self.log = []

    def on_for_rotations(self, left_speed, right_speed, rotations):
        self.log.append(('on_for_rotations', repr(left_speed), repr(right_speed), rotations))


