#!/usr/bin/env python3
import unittest
from R_ev3dev import ev3_interpreter


class TestColor(unittest.TestCase):
    def test_get_value(self):
        i = ev3_interpreter()
        color = i.evaluate_internal("color 1 on #1").value
        self.assertEqual(color.color, 0)
        color.color = 9
        color_value = i.evaluate("color 1 color")
        self.assertEqual(color_value, 'value int 9')

