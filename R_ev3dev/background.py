from queue import Queue
from threading import Thread
from enum import Enum
import time
from R_ev3dev.interpreter import Command


class Signal(Enum):
    POISON_PILL = 0


class Function(object):
    def __init__(self, func, args):
        self.__function = func
        self.__args = args

    def execute(self):
        self.__function(*self.__args)


class StoppedException(Exception):
    """  this exception is raised by any action after
         the runner was stopped """


class UnknownMessageException(Exception):
    """  this exception is raised if the runner
         can not handle the message type"""


class BackgroundRunner(object):
    def __init__(self):
        self.__queue = Queue()
        self.__thread = Thread(target=self.__schedule, args=[])
        self.__thread.start()

    def __schedule(self):
        while True:
            message = self.__queue.get()
            if message == Signal.POISON_PILL:
                break
            elif isinstance(message, Function):
                message.execute()

    def run_later(self, func, *args):
        if not callable(func):
            raise UnknownMessageException("unknown message: {}".format(func))
        if self.is_stopped():
            raise StoppedException("runner is stopped")
        self.__queue.put(Function(func, args))

    def is_stopped(self):
        return not self.__queue

    def stop(self):
        if self.is_stopped():
            raise StoppedException("runner is already stopped")
        self.__queue.put(Signal.POISON_PILL)
        self.__thread.join()
        self.__queue = None
        self.__thread = None


class NestedBackgroundError(Exception):
    """ will be raised if the client tries to nest bg calls """


class Sleep(Command):
    """ sleep for seconds

        sleep <seconds> - sleep for seconds (float)
    """
    def __init__(self, name):
        super().__init__(name)

    def invoke(self, interpreter_context, args):
        seconds = float(args[0])
        time.sleep(seconds)


class ToBackground(Command):
    """ run command in the background

        bg <command string> - runs the command in the background
        bg                  - wait until all background processes are complete
    """
    def __init__(self, name):
        super().__init__(name)
        self.__background_runner = None

    def __schedule(self, interpreter, command_string):
        if self.__background_runner is None:
            self.__background_runner = BackgroundRunner()
        self.__background_runner.run_later(
            interpreter.evaluate,
            command_string
        )

    def invoke(self, interpreter_context, args):
        if len(args):
            if args[0].strip() == self.name:
                raise NestedBackgroundError("nested calls of bg are not allowed!")
            command_string = " ".join(args)
            self.__schedule(interpreter_context.interpreter, command_string)
        else:
            self.__background_runner.stop()
            self.__background_runner = None
