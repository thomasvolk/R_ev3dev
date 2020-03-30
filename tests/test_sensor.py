#!/usr/bin/env python3
import unittest
from R_ev3dev import ev3_interpreter


class TestInfrared(unittest.TestCase):
    def test_get_value_with_channel(self):
        i = ev3_interpreter()
        i.evaluate_internal("infrared 1 on #1")
        ir_value = i.evaluate("infrared 1 distance 2")
        self.assertEqual(ir_value, 'value int 46')

    def test_get_value_without_channel(self):
        i = ev3_interpreter()
        i.evaluate_internal("infrared 1 on #1")
        ir_value = i.evaluate("infrared 1 distance")
        self.assertEqual(ir_value, 'value int 45')


class TestColor(unittest.TestCase):
    def test_get_value(self):
        i = ev3_interpreter()
        color = i.evaluate_internal("color 1 on #1").value
        self.assertEqual(color.color, 0)
        color.color = 9
        color_value = i.evaluate("color 1 color")
        self.assertEqual(color_value, 'value int 9')

