from abc import ABC, abstractmethod


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
    def invoke(self, args):
        """
        abstract method for command execution

        :param args: arguments
        :return: command result
        """


class Interpreter(object):
    def __init__(self, items):
        self._commands = {item.name: item for item in items if isinstance(item, Command)}
        self._references = {item.key: item for item in items if isinstance(item, Reference)}

    def _resolve_reference(self, item):
        ref = self._references.get(item)
        if ref:
            return ref.value
        return item

    def evaluate(self, line):
        try:
            return str(self.evaluate_internal(line))
        except Exception as e:
            return 'error {} {}'.format(e.__class__.__name__, str(e))

    def evaluate_internal(self, line):
        stripped_line = line.strip()
        if not stripped_line:
            raise KeyError(stripped_line)
        if stripped_line.startswith('#'):
            return ""
        arg_str = ""
        parts = stripped_line.split(' ', 1)
        cmd_name = parts[0]
        if len(parts) > 1:
            arg_str = parts[1]
        command = self._commands[cmd_name]
        args = [self._resolve_reference(a) for a in arg_str.split()]
        return EvaluationResult(command.invoke(args))


VALUE_CONVERTER = {
    int: lambda v: str(v),
    float: lambda v: str(v),
    str: lambda v: v,
}


class EvaluationResult(object):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        t = type(self.value)
        value_converter = VALUE_CONVERTER.get(t)
        if value_converter:
            return "value {} {}".format(t.__name__, value_converter(self.value))
        return "ok"
