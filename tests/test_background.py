#!/usr/bin/env python3
import unittest
from R_ev3dev.background import BackgroundRunner, StoppedException, UnknownMessageException


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
