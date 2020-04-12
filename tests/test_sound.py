#!/usr/bin/env python3
import unittest
from R_ev3dev import ev3_interpreter
from R_ev3dev.ev3 import sound


class TestSpeak(unittest.TestCase):
    def test_get_value(self):
        i = ev3_interpreter()
        i.evaluate_internal("speak Hello World").value
        self.assertEqual(sound.get_spoken(), ["Hello World"])

