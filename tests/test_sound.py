#!/usr/bin/env python3
import unittest
from R_ev3dev import ev3_interpreter
from R_ev3dev.ev3 import sound


class TestSpeak(unittest.TestCase):
    def setUp(self):
        sound.clear_spoken()

    def test_speak(self):
        i = ev3_interpreter()
        i.evaluate_internal("speak Hello World")
        self.assertEqual(sound.get_spoken(), ["Hello World"])

