from R_ev3dev.interpreter import Interpreter, Command, Reference
from R_ev3dev.motor import Tank
from R_ev3dev.sensor import Color
from R_ev3dev.server import Server
from R_ev3dev.ev3 import ev3dev2
import logging, os


class NoOperation(Command):
    def invoke(self, args):
        return None


def ev3_interpreter():
    return Interpreter([
        Reference('A', ev3dev2.motor.OUTPUT_A),
        Reference('B', ev3dev2.motor.OUTPUT_B),
        Reference('C', ev3dev2.motor.OUTPUT_C),
        Reference('D', ev3dev2.motor.OUTPUT_D),
        Reference('1', ev3dev2.sensor.INPUT_1),
        Reference('2', ev3dev2.sensor.INPUT_2),
        Reference('3', ev3dev2.sensor.INPUT_3),
        Reference('4', ev3dev2.sensor.INPUT_4),
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
