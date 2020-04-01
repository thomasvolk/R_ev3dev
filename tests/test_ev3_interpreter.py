#!/usr/bin/env python3
import unittest
from R_ev3dev import ev3_interpreter
from R_ev3dev.server import CloseException


class TestEv3Interpreter(unittest.TestCase):
    def test_hello(self):
        i = ev3_interpreter()
        self.assertEqual(i.evaluate("hello"), "ok")

    def test_close(self):
        i = ev3_interpreter()
        self.assertRaises(CloseException, i.evaluate, "close")
