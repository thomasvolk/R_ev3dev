from R_ev3dev.interpreter import Command
from R_ev3dev import version


class Version(Command):
    """ show version """
    def invoke(self, interpreter_context, args):
        return version.VERSION


class Help(Command):
    """ show help """

    def _doc(self, item):
        return item.__doc__.strip() if item.__doc__ else ''

    def _line(self, item):
        return "{} - {}".format(item.name, self._doc(item).split("\n")[0])

    def _overview(self, commands):
        command_lines = [self._line(c) for c in commands]
        return """---

  R_ev3 protocol language version {}

    author: Thomas Volk
    license: Apache License Version 2.0
    source: https://github.com/thomasvolk/R_ev3dev

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
            return self._details(interpreter_context.interpreter.commands[cmd])
        else:
            return self._overview(interpreter_context.interpreter.commands.values())
