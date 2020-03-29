from R_ev3dev.interpreter import Interpreter, Command, Reference
from R_ev3dev.motor import Tank, MediumMotor
from R_ev3dev.sensor import Color, Infrared
from R_ev3dev.server import Server, CloseException
from R_ev3dev import version
from ev3dev2 import motor, sensor
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


class Version(Command):
    """ show version """
    def invoke(self, interpreter_context, args):
        return version.VERSION


class Help(Command):
    """ show help """

    def _doc(self, item):
        return item.__doc__.strip() if item.__doc__ else ''

    def _overview(self, commands):
        def _line(item):
            return "{} - {}".format(item.name, self._doc(item).split("\n")[0])
        command_lines = [_line(c) for c in commands]
        return """---

  R_ev3 protocol language version {}

  possible commands:

    {} 

  use help <command> for details
  
---""".format(version.VERSION, '\n    '.join(command_lines))

    def _details(self, command):
        return """---

  {}
  
  {}        

---""".format(command.name, self._doc(command))

    def invoke(self, interpreter_context, args):
        if len(args) > 0:
            cmd = args[0]
            return self._details(interpreter_context.commands[cmd])
        else:
            return self._overview(interpreter_context.commands.values())


def ev3_interpreter():
    return Interpreter([
        Help("help"),
        Version("version"),
        Hello("hello"),
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
