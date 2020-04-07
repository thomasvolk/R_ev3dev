from R_ev3dev.interpreter import Command, Item, string_to_bool
from R_ev3dev.background import BackgroundRunner
from abc import ABC, abstractmethod


class PeripheralAction(ABC, Item):
    @abstractmethod
    def invoke(self, context, args):
        """
        abstract method for peripheral action execution

        :param context: context of the peripheral command
        :param args: arguments
        :return: action result
        """


class PeripheralCommand(Command):
    def __init__(self, name, actions):
        self.__actions = {a.name: a for a in actions}
        self.__context = {}
        super().__init__(name)

    def invoke(self, interpreter_context,  args):
        peripheral_id = args[0]
        action = args[1]
        context = self.__context.setdefault(peripheral_id, {})
        return self.__actions[action].invoke(context, args[2:])


class RunInBackground(PeripheralAction):
    def __init__(self, command):
        self.__command = command
        super().__init__("run_in_background")

    def invoke(self, context, args):
        if len(args) > 0:
            self.__command.set_run_in_background(string_to_bool(args[0]))
        else:
            return self.__command.get_run_in_background()


class BackgroundProxy(PeripheralAction):
    def __init__(self, command, target):
        self.__target = target
        self.__command = command
        super().__init__(target.name)

    def invoke(self, context, args):
        self.__command.run_in_background(self.__target.invoke, context, args)


class BackgroundPeripheralCommand(PeripheralCommand):
    def __init__(self, name, actions):
        actions.append(RunInBackground(self))
        self.__background_runner = None
        super().__init__(name, actions)

    def run_in_background(self, func, context, args):
        if self.get_run_in_background():
            self.__background_runner.run_later(func, *(context, args))
        else:
            func(context, args)

    def get_run_in_background(self):
        return self.__background_runner is not None

    def set_run_in_background(self, active):
        if active:
            self.__background_runner = BackgroundRunner()
        else:
            self.__background_runner.stop()
            self.__background_runner = None

    def with_background_proxy(self, target):
        return BackgroundProxy(self, target)
