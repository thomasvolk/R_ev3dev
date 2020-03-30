#!/usr/bin/env python3
import unittest
from R_ev3dev.interpreter import Interpreter, Command
from R_ev3dev.help import Help, Version


class TestCommand01(Command):
    """ this is the test command 01

        usage:
          c01
    """
    def invoke(self, interpreter_context, args):
        return 1


class TestCommand02(Command):
    """ this is the test command 02

    """
    def invoke(self, interpreter_context, args):
        return 2


class TestCommand03(Command):
    def invoke(self, interpreter_context, args):
        return 3


class TestHelp(unittest.TestCase):
    def setUp(self):
        self.interpreter = Interpreter([
            TestCommand01('c01'),
            TestCommand02('c02'),
            TestCommand03('c03'),
            Help('help'),
            Version('version')
        ])

    def test_overview(self):
        self.assertEqual("""---

  R_ev3 protocol language version 0.0.1

  possible commands:

    c01 - this is the test command 01
    c02 - this is the test command 02
    c03 - 
    help - show help
    version - show version 

  use help <command> for details

---""", self.interpreter.evaluate_internal("help").value)

    def test_help(self):
        self.assertEqual("""---

  c01

  this is the test command 01

        usage:
          c01        

---""", self.interpreter.evaluate_internal("help c01").value)

    def test_version(self):
        self.assertEqual('0.0.1', self.interpreter.evaluate_internal("version").value)