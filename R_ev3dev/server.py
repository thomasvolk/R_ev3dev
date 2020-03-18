from threading import Thread
import socket, logging


class Connection(object):
    def __init__(self, interpreter, buffer_size):
        self.__buffer_size = buffer_size
        self.__interpreter = interpreter

    def __call__(self, *args, **kwargs):
        conn = args[0]
        addr = args[1]
        logging.info("open connection {}".format(addr))
        with conn:
            while True:
                data = conn.recv(self.__buffer_size)
                if not data or data == b'\x04':
                    break
                request = data.decode()
                logging.info("<= {}".format(request.strip()))
                response = "{}\n".format(self.__interpreter.evaluate(request))
                logging.info("=> {}".format(response.strip()))
                conn.sendall(response.encode())
        logging.info("close connection {}".format(addr))


class Server(object):
    def __init__(self,
                 interpreter_factory,
                 host='',
                 port=9999,
                 buffer_size=2048,
                 connection_backlog_size=2):
        self.__host = host
        self.__port = port
        self.__buffer_size = buffer_size
        self.__interpreter_factory = interpreter_factory
        self.__connection_backlog_size = connection_backlog_size
        self.__connections = []

    def run(self):
        logging.info("start server host={} port={}".format(self.__host, self.__port))
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.__host, self.__port))
            s.listen(self.__connection_backlog_size)
            while True:
                conn, addr = s.accept()
                t = Thread(target=Connection(self.__interpreter_factory(), self.__buffer_size), args=(conn, addr))
                self.__connections.append(t)
                t.start()
