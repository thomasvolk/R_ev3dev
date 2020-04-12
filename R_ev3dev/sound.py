from R_ev3dev.interpreter import Command
from R_ev3dev.ev3 import sound


class Speak(Command):
    """ let the robot speak text """
    def invoke(self, interpreter_context, args):
        s = sound.Sound()
        text = " ".join(args)
        s.speak(text)
