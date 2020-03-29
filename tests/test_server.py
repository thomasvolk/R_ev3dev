#!/usr/bin/env python3
import unittest
from socket_mock import MockSocketConnection, MockServerSocketModule
from R_ev3dev.server import Server


def mock_interpreter_factory():
    class MockInterpreter(object):
        def evaluate(self, cmd):
            return "ok"
    return MockInterpreter()


class TestServer(unittest.TestCase):
    def test_add_client(self):
        sf = MockServerSocketModule()
        conn = MockSocketConnection()
        server = Server(mock_interpreter_factory, socket_lib=sf)
        server.add_client(conn, ('test_client', 12345))
