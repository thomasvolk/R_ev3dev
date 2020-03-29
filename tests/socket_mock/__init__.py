from socket_mock.socket import MockSocket, MockSocketConnection

AF_INET = 0
SOCK_STREAM = 1


def socket(family=-1, type=-1, proto=-1, fileno=None):
    return MockSocket(family=family, type=type, proto=proto, fileno=fileno)


class MockServerSocketModule:
    def __init__(self):
        self.__sockets = []

    @property
    def sockets(self):
        return self.__sockets

    def socket(self, family=-1, type=-1, proto=-1, fileno=None):
        s = socket(family=family, type=type, proto=proto, fileno=fileno)
        self.__sockets.append(s)
        return s
