from ev3dev2_mock.sensor import lego

INPUT_1 = 'in1'
INPUT_2 = 'in2'
INPUT_3 = 'in3'
INPUT_4 = 'in4'


class Sensor(object):
    def __init__(self, address, device_name):
        self.address = address
        self.device_name = device_name


def list_sensors():
    return iter([
        Sensor(INPUT_1, 'lego-ev3-touch'),
        Sensor(INPUT_2, 'lego-ev3-ir'),
        Sensor(INPUT_3, 'lego-ev3-color'),
    ])
