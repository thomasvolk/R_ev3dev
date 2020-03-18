from R_ev3dev.interpreter import Interpreter, Command, Reference
from R_ev3dev.motor import Tank
from R_ev3dev.sensor import Color
from R_ev3dev.server import Server
from R_ev3dev.ev3 import ev3dev2
from ev3dev2 import motor, sensor
import logging, os


class NoOperation(Command):
    def invoke(self, args):
        return None


def ev3_interpreter():
    return Interpreter([
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
        NoOperation("hello")
    ])


def server(host='',
           port=9999,
           buffer_size=2048,
           connection_backlog_size=2):
    logging.basicConfig(level=os.environ.get("LOGLEVEL", "WARN"))
    return Server(ev3_interpreter,
                  host=host,
                  port=port,
                  buffer_size=buffer_size,
                  connection_backlog_size=connection_backlog_size)
