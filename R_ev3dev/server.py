from threading import Thread, RLock
import socket, logging


class CloseException(Exception):
    """ this exception will close the connection """


class Connection(object):
    def __init__(self, interpreter, buffer_size):
        self.__buffer_size = buffer_size
        self.__interpreter = interpreter

    def __call__(self, server, conn, addr):
        server.register_client(self)
        try:
            def _log(msg, *log_args):
                logging.info("connection({}:{}) {}".format(addr[0], addr[1], msg.format(*log_args)))

            _log("open")
            with conn:
                while True:
                    data = conn.recv(self.__buffer_size)
                    if not data or data == b'\x04':
                        break
                    request = data.decode()
                    _log("<= {}", request.strip())
                    try:
                        response = self.__interpreter.evaluate(request)
                        if response:
                            response_data = "{}\n".format(response)
                            _log("=> {}", response_data.strip())
                            conn.sendall(response_data.encode())
                    except CloseException:
                        break
            _log("close")
        finally:
            server.unregister_client(self)


class Server(object):
    def __init__(self,
                 interpreter_factory,
                 host='',
                 port=9999,
                 buffer_size=2048,
                 max_clients=1):
        self.__host = host
        self.__port = port
        self.__buffer_size = buffer_size
        self.__interpreter_factory = interpreter_factory
        self.__max_clients = max_clients
        self.__clients = []
        self.__rlock = RLock()

    def register_client(self, con):
        self.__rlock.acquire()
        self.__clients.append(con)
        self.__rlock.release()

    def unregister_client(self, con):
        self.__rlock.acquire()
        try:
            self.__clients.remove(con)
        finally:
            self.__rlock.release()

    def run(self):
        logging.info("start server host={} port={} max-clients={}".format(self.__host, self.__port, self.__max_clients))
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.__host, self.__port))
            s.listen()
            while True:
                conn, addr = s.accept()
                if len(self.__clients) < self.__max_clients:
                    connection = Connection(self.__interpreter_factory(), self.__buffer_size)
                    t = Thread(target=connection, args=(self, conn, addr))
                    t.start()
                else:
                    conn.sendall("error to many clients".encode())
                    conn.close()
