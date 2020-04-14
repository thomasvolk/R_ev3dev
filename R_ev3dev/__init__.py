from R_ev3dev.interpreter import Interpreter, Command, Reference
from R_ev3dev.motor import Tank, MediumMotor, LargeMotor, ListMotors
from R_ev3dev.sensor import Color, Infrared, Touch, Gyro, ListSensors
from R_ev3dev.sound import Speak
from R_ev3dev.background import ToBackground, Sleep
from R_ev3dev.server import Server, CloseException
from R_ev3dev.help import Version, Help
from R_ev3dev.ev3 import motor, sensor
import logging
import os


class Hello(Command):
    """ hello command to test the server response

        expected response: ok
    """
    def invoke(self, interpreter_context, args):
        return None


class Close(Command):
    """ this command closes the connection to the server """
    def invoke(self, interpreter_context, args):
        interpreter_context.throw(CloseException())


def ev3_interpreter():
    return Interpreter([
        Help("help"),
        Version("version"),
        Hello("hello"),
        Close("close"),
        ToBackground("bg"),
        Sleep("sleep"),
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
        Gyro("gyro"),
        Touch("touch"),
        MediumMotor("medium_motor"),
        LargeMotor("large_motor"),
        ListMotors("list_motors"),
        ListSensors("list_sensors"),
        Speak("speak")
    ])


def server(host='',
           port=9999,
           buffer_size=2048,
           max_clients=1,
           log_level='WARN'):
    logging.basicConfig(level=os.environ.get("LOGLEVEL", log_level))
    return Server(ev3_interpreter,
                  host=host,
                  port=port,
                  buffer_size=buffer_size,
                  max_clients=max_clients)
