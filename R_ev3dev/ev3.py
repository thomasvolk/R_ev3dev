from importlib.util import find_spec

if find_spec('ev3dev2_mock'):
    import ev3dev2_mock as ev3dev2
else:
    import ev3dev2
