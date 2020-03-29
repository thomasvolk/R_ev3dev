class MockSocketConnection(object):

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
    def __init__(self, family=-1, type=-1, proto=-1, fileno=None, response_map={}):
        self.__response_map = response_map
        self.family = family
        self.type = type
        self.proto = proto
        self.fileno = fileno
        self.address = None
        self.log = []
        self.__last_received = None

    def connect(self, addr):
        self.address = addr

    def bind(self, addr):
        pass

    def listen(self):
        pass

    def accept(self):
        return MockSocketConnection(), ('test_client', 8888)

    def close(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass