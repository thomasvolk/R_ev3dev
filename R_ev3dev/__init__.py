from R_ev3dev.interpreter import Interpreter, Command, Reference
from R_ev3dev.motor import Tank, MediumMotor
from R_ev3dev.sensor import Color, Infrared
from R_ev3dev.server import Server, CloseException
from ev3dev2 import motor, sensor
import logging, os


class NoOperation(Command):
    def invoke(self, interpreter_obj, args):
        return None


class Close(Command):
    def invoke(self, interpreter_obj, args):
        interpreter_obj.throw(CloseException())


def ev3_interpreter():
    return Interpreter([
        NoOperation("hello"),
        Close("close"),
        Reference('A', motor.OUTPUT_A),
        Reference('B', motor.OUTPUT_B),
        Reference('C', motor.OUTPUT_C),
        Reference('D', motor.OUTPUT_D),
        Reference('1', sensor.INPUT_1),
        Reference('2', sensor.INPUT_2),
        Reference('3', sensor.INPUT_3),
        Reference('4', sensor.INPUT_4),
        Tank("tank"),
        Color("color"),
        Infrared("infrared"),
        MediumMotor("medium_motor")
    ])


def server(host='',
           port=9999,
           buffer_size=2048,
           max_clients=1):
    logging.basicConfig(level=os.environ.get("LOGLEVEL", "WARN"))
    return Server(ev3_interpreter,
                  host=host,
                  port=port,
                  buffer_size=buffer_size,
                  max_clients=max_clients)
