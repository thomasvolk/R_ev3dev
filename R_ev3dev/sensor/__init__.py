from R_ev3dev.sensor.color import Color
from R_ev3dev.sensor.infrared import Infrared
from R_ev3dev.interpreter import Command
from R_ev3dev.ev3 import ev3dev2


class ListSensors(Command):
    """ list all sensors """
    def invoke(self, interpreter_context, args):
        return [{'driver_name': s.driver_name, 'address': s.address} for s in ev3dev2.sensor.list_sensors()]
