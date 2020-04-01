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


class TestGyro(unittest.TestCase):
    def test_angle(self):
        i = ev3_interpreter()
        gyro = i.evaluate_internal("gyro 1 on #1").value
        self.assertEqual(gyro.angle, 45)
        gyro.angle = 90
        value = i.evaluate("gyro 1 angle")
        self.assertEqual(value, 'value int 90')


class TestTouch(unittest.TestCase):
    def test_is_pressed(self):
        i = ev3_interpreter()
        touch = i.evaluate_internal("touch 1 on #1").value
        self.assertEqual(touch.is_pressed, True)
        touch.is_pressed = False
        value = i.evaluate("touch 1 is_pressed")
        self.assertEqual(value, 'value boolean False')


class TestListSensors(unittest.TestCase):
    def test_list(self):
        i = ev3_interpreter()
        self.assertEqual(i.evaluate_internal('list_sensors').value, [
            {'address': 'in1', 'driver_name': 'lego-ev3-touch'},
            {'address': 'in2', 'driver_name': 'lego-ev3-ir'},
            {'address': 'in3', 'driver_name': 'lego-ev3-color'},
        ])
