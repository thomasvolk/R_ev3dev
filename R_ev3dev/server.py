from threading import Thread, RLock
import socket, logging


class CloseException(Exception):
    """ this exception will close the connection """


class Connection(object):
    def __init__(self, server, socket_connection, client_address, interpreter, buffer_size):
        self.__buffer_size = buffer_size
        self.__interpreter = interpreter
        self.__socket_connection = socket_connection
        self.__client_address = client_address
        self.__server = server

    def _log(self, msg, *log_args):
        logging.info("connection({}:{}) {}".format(
            self.__client_address[0],
            self.__client_address[1],
            msg.format(*log_args))
        )

    def receive(self):
        data = self.__socket_connection.recv(self.__buffer_size)
        if not data or data == b'\x04':
            raise CloseException()
        return data.decode()

    def send(self, response_data):
        self.__socket_connection.sendall(response_data.encode())

    def __call__(self):
        self.__server.register_client(self)
        try:
            self._log("open")
            with self.__socket_connection:
                while True:
                    try:
                        request = self.receive()
                        self._log("<= {}", request.strip())
                        response = self.__interpreter.evaluate(request)
                        if response:
                            response_data = "{}\n".format(response)
                            self._log("=> {}", response_data.strip())
                            self.send(response_data)
                    except CloseException:
                        break
            self._log("close")
        finally:
            self.__server.unregister_client(self)


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
                    connection = Connection(
                        self,
                        conn,
                        addr,
                        self.__interpreter_factory(),
                        self.__buffer_size
                    )
                    t = Thread(target=connection, args=[])
                    t.start()
                else:
                    conn.sendall("error to many clients".encode())
                    conn.close()
