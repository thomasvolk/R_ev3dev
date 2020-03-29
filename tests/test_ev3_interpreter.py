#!/usr/bin/env python3
import unittest
from R_ev3dev import ev3_interpreter


class TestEv3Interpreter(unittest.TestCase):
    def test_hello(self):
        i = ev3_interpreter()
        self.assertEqual(i.evaluate("hello"), "ok")
