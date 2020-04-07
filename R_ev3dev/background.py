from queue import Queue
from threading import Thread
from enum import Enum


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
        if not self.__queue:
            raise StoppedException("runner is stopped")
        self.__queue.put(Function(func, args))

    def stop(self):
        if not self.__queue:
            raise StoppedException("runner is already stopped")
        self.__queue.put(Signal.POISON_PILL)
        self.__thread.join()
        self.__queue = None
        self.__thread = None
