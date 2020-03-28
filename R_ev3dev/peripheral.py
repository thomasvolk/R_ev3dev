from R_ev3dev.interpreter import Command, Item
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

    def invoke(self, interpreter_obj,  args):
        peripheral_id = args[0]
        action = args[1]
        context = self.__context.setdefault(peripheral_id, {})
        return self.__actions[action].invoke(context, args[2:])

