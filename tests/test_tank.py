#!/usr/bin/env python3
import unittest
from R_ev3dev import ev3_interpreter


class TestTank(unittest.TestCase):
    def test_on_for_rotations(self):
        i = ev3_interpreter()
        move_tank = i.evaluate_internal("tank 1 on #A #B").value
        self.assertEqual(move_tank.left_motor_port, 'outA')
        self.assertEqual(move_tank.right_motor_port, 'outB')
        i.evaluate("tank 1 on_for_rotations 10 10 1")
        self.assertEqual(move_tank.log, [('on_for_rotations', 'SpeedPercent(10)', 'SpeedPercent(10)', 1)])
