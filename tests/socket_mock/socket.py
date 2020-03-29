

class MockSocketConnection(object):

    def do_receive(self, msg):
        self.__recv_queue.put(msg)

    def sendall(self, msg):
        pass

    def recv(self, buffer_size):
        return b'\x04'

    def close(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass


class MockSocket(object):
    def __init__(self, family=-1, type=-1, proto=-1, fileno=None):
        self.family = family
        self.type = type
        self.proto = proto
        self.fileno = fileno
        self.address = None
        self.__connections = []

    def connect(self, addr):
        self.address = addr

    def bind(self, addr):
        pass

    def listen(self):
        pass

    def accept(self):
        connection = MockSocketConnection()
        self.__connections.append(connection)
        return connection, ('test_client', 8888)

    @property
    def connections(self):
        return self.__connections

    def close(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass