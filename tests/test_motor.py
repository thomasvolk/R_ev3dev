#!/usr/bin/env python3
import unittest
from R_ev3dev import ev3_interpreter


class TestMediumMotor(unittest.TestCase):
    def test_on_for_rotations(self):
        i = ev3_interpreter()
        mm = i.evaluate_internal("medium_motor 1 on #A").value
        self.assertEqual(mm.address, 'outA')
        i.evaluate("medium_motor 1 on_for_rotations 10 1")
        self.assertEqual(mm.log, [('on_for_rotations', 'SpeedPercent(10)', 1)])


class TestLargeMotor(unittest.TestCase):
    def test_on_for_rotations(self):
        i = ev3_interpreter()
        lm = i.evaluate_internal("large_motor 2 on #D").value
        self.assertEqual(lm.address, 'outD')
        i.evaluate("large_motor 2 on_for_rotations 10 2")
        self.assertEqual(lm.log, [('on_for_rotations', 'SpeedPercent(10)', 2)])
