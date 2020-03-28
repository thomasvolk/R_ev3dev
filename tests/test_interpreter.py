#!/usr/bin/env python3
import unittest
from R_ev3dev.interpreter import Interpreter, Command, Reference


class TestCommandInt(Command):
    def invoke(self, interpreter_obj, args):
        return 1


class TestCommandFloat(Command):
    def invoke(self, interpreter_obj, args):
        return 1.0


class TestCommandStr(Command):
    def invoke(self, interpreter_obj, args):
        return "Hello World"


class BaseTestCommand(Command):
    def invoke(self, interpreter_obj, args):
        return self.__class__.__name__, args


class Test01Command(BaseTestCommand):
    pass


class Test02Command(BaseTestCommand):
    pass


class Test03Command(BaseTestCommand):
    pass


class TestInterpreter(unittest.TestCase):
    def test_evaluate_internal(self):
        i = Interpreter([
            Test01Command('test01'),
            Test02Command('test02'),
            Test03Command('test03'),
            Reference('X', 2),
            Reference('Y', 100)
        ])
        self.assertEqual(i.evaluate_internal("test01 1 #X 3").value, ('Test01Command', ['1', 2, '3']))
        self.assertEqual(i.evaluate_internal("test02 #X   #Y ").value, ('Test02Command', [2, 100]))
        self.assertEqual(i.evaluate_internal("test03  ").value, ('Test03Command', []))
        self.assertEqual(i.evaluate_internal("  "), '')
        self.assertEqual(i.evaluate_internal("  # 123"), '')
        self.assertRaises(KeyError, i.evaluate_internal, "x")

    def test_evaluate(self):
        i = Interpreter([
            Test01Command('test01'),
            Reference('X', 2),
            TestCommandInt("test_int"),
            TestCommandFloat("test_float"),
            TestCommandStr("test_str"),
        ])
        self.assertEqual(i.evaluate("test_int"), "value int 1")
        self.assertEqual(i.evaluate("test_float"), "value float 1.0")
        self.assertEqual(i.evaluate("test_str"), "value str Hello World")
        self.assertEqual(i.evaluate("test01 1 #X 3"), "ok")
        self.assertEqual(i.evaluate("x"), "error KeyError 'x'")

