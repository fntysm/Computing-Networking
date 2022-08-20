import signal
import socket
import threading


class Server:
    # creating a socket for the incoming connections, we bind the socket and wait for the client to connect
    def __init__(self, config):
        # The signal.signal() function allows defining custom handlers to be executed when a signal is received.
        # SIGINT is translated into a KeyboardInterrupt exception
        signal.signal(signal.SIGINT, self.shutdown)
        # Create a TCP socket, the arguments passed in are the address family and socket type respectively
        # AF_INET is the Internet address family for IPv4. SOCK_STREAM is the socket type for TCP.
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Re-use the socket
        # (level, option_name, value: int)
        # (the socket layer itself, it allows the socket to bind to a port even if in use by another socket ,)
        self.serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # bind the socket to a public host or a port
        # ADDRESS OF BIND PORT
        self.serverSocket.bind(config['BIND_PORT'])
        # Enable a server to accept connections,
        self.serverSocket.listen(10)
        self.clients = {}

    def clientListen(self):
        while True:
            # Establishing the connection
            (clientsocket, clientaddress) = self.serverSocket.accept()
            # the callable object is the target, name is the threadName
            # A thread is a separate flow of execution. This means that your program will have two things happening at once.
            d = threading.Thread(name=self.getClient(clientaddress), target=self.proxyThread,
                                 args=(clientsocket, clientaddress))
            # The main purpose of a daemon thread is to execute background task especially in case of some routine periodic task or work.
            d.setDaemon(True)
            d.start()
