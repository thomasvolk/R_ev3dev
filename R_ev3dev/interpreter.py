from abc import ABC, abstractmethod
import json


def string_to_bool(s):
    return s.strip().lower() == 'true'


class Item(object):
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name


class Reference(Item):
    def __init__(self, name, value, prefix = '#'):
        self.__value = value
        self.__prefix = prefix
        super().__init__(name)

    @property
    def key(self):
        return "{}{}".format(self.__prefix, self.name)

    @property
    def value(self):
        return self.__value


class Command(Item, ABC):
    @abstractmethod
    def invoke(self, interpreter_context, args):
        """
        abstract method for command execution

        :param interpreter_context: interpreter context
        :param args: arguments
        :return: command result
        """


class Interpreter(object):
    class Context(object):
        def __init__(self, interpreter):
            self.__interpreter = interpreter

        @property
        def commands(self):
            return self.__interpreter.commands

        def throw(self, e):
            raise Interpreter.WrapperException(e)

    class WrapperException(Exception):
        """
        interpreter exception

        if this exception will be raised by the Interpreter.raise_exception method,
        the interpreter will raise the
        """
        def __init__(self, origin):
            self.origin = origin
            super()

    def __init__(self, items):
        self._commands = {item.name: item for item in items if isinstance(item, Command)}
        self._references = {item.key: item for item in items if isinstance(item, Reference)}
        self._context = Interpreter.Context(self)

    def _resolve_reference(self, item):
        ref = self._references.get(item)
        if ref:
            return ref.value
        return item

    @property
    def commands(self):
        return self._commands

    def evaluate(self, line):
        try:
            return str(self.evaluate_internal(line))
        except Interpreter.WrapperException as ie:
            raise ie.origin
        except Exception as e:
            return 'error {} {}'.format(e.__class__.__name__, str(e))

    def evaluate_internal(self, line):
        stripped_line = line.strip()
        arg_str = ""
        parts = stripped_line.split(' ', 1)
        cmd_name = parts[0]
        if len(parts) > 1:
            arg_str = parts[1]
        command = self._commands[cmd_name]
        args = [self._resolve_reference(a) for a in arg_str.split()]
        return EvaluationResult(command.invoke(self._context, args))


VALUE_CONVERTER = {
    int: lambda v: ('int', str(v)),
    float: lambda v: ('float', str(v)),
    str: lambda v: ('str', v),
    bool: lambda v: ('boolean', str(v)),
    dict: lambda d: ('json', json.dumps(d)),
    list: lambda d: ('json', json.dumps(d))
}


class EvaluationResult(object):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        value_converter = VALUE_CONVERTER.get(type(self.value))
        if value_converter:
            t, v = value_converter(self.value)
            return "value {} {}".format(t, v)
        return "ok"
