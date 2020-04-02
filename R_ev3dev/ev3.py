from importlib.util import find_spec

if find_spec('ev3dev2_mock'):
    import ev3dev2_mock as ev3dev2
    from ev3dev2_mock.sensor import lego as lego_sensor
else:
    import ev3dev2
    from ev3dev2.sensor import lego as lego_sensor
