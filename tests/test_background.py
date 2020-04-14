#!/usr/bin/env python3
import unittest
from R_ev3dev.background import BackgroundRunner, StoppedException, UnknownMessageException, NestedBackgroundError
from R_ev3dev import ev3_interpreter
from R_ev3dev.ev3 import sound


class TestBackgroundRunner(unittest.TestCase):

    def setUp(self):
        self.count = 0

    def increase_count(self, amount=1):
        self.count = self.count + amount

    def test_run_functions(self):
        br = BackgroundRunner()
        br.run_later(self.increase_count)
        br.run_later(self.increase_count, 9)
        br.stop()
        self.assertEqual(10, self.count)

    def test_stopped(self):
        br = BackgroundRunner()
        br.stop()
        self.assertRaises(StoppedException, br.run_later, lambda: None)
        self.assertRaises(StoppedException, br.stop)

    def test_unknown_message(self):
        br = BackgroundRunner()
        self.assertRaises(UnknownMessageException, br.run_later, "?")
        br.stop()


class TestToBackground(unittest.TestCase):
    def setUp(self):
        sound.clear_spoken()

    def test_bg(self):
        i = ev3_interpreter()
        i.evaluate_internal("bg sleep 0.1")
        i.evaluate_internal("bg speak Hello World")
        i.evaluate_internal("bg sleep 0.1")
        i.evaluate_internal("bg speak The End")
        i.evaluate_internal("bg")
        self.assertEqual(sound.get_spoken(), ["Hello World", "The End"])

    def test_nested_bg(self):
        i = ev3_interpreter()
        self.assertRaises(NestedBackgroundError, i.evaluate_internal, "bg bg sleep 0.1")

