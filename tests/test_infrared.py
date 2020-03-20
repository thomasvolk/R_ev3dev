#!/usr/bin/env python3
import unittest
from R_ev3dev import ev3_interpreter


class TestInfrared(unittest.TestCase):
    def test_get_value(self):
        i = ev3_interpreter()
        ir = i.evaluate_internal("infrared 1 on #1").value
        ir_value = i.evaluate("infrared 1 distance 1")
        self.assertEqual(ir_value, 'value int 45')

