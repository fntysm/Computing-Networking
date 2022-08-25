import signal
import socket
import threading
import sys

config = {
    'HOST_NAME': '',
    'BIND_PORT': '',
    'MAX_REQUEST_LEN': '',
    'CONNECTION_TIMEOUT' : 10
}


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
        self.serverSocket.bind((config['HOST_NAME'], config['BIND_PORT']))
        # Enable a server to accept connections, we chose 10 clients
        self.serverSocket.listen(10)
        self.clients = {}

    def clientListen(self):
        while True:
            # Establishing the connection
            (clientsocket, clientaddress) = self.serverSocket.accept()
            # the callable object is the target, name is the threadName
            # A thread is a separate flow of execution. This means that your program will have two things happening at once.
            d = threading.Thread(name=self.getClient(clientaddress), target=self.proxyTraffic,
                                 args=(clientsocket, clientaddress))
            # The main purpose of a daemon thread is to execute background task especially in case of some routine periodic task or work.
            d.setDaemon(True)
            d.start()

    def proxyTraffic(self, connection, clientAddress, config):
        # here we get the request from the browser
        # .recv() is to receive data from TCP and UDP sockets
        global s
        request = connection.recv(config['MAX_REQUEST_LEN'])
        # here we retrieve the first line
        first_line = request.split('\n')[0]
        url = first_line.split(' ')[1]
        # to get the address of the requested website
        httpCheck = url.find('://')
        if httpCheck==-1:
            temp = url
        else:
            temp = url[(httpCheck+3):]
        # find the port position
        portCheck = temp.find(":")
        # and now we have to find the end of the webserver
        webserverCheck = temp.find('/')
        if webserverCheck==-1:
            webserverCheck = len(temp)
        webserver = ""
        port = -1
        if (portCheck==-1 or webserverCheck<portCheck):
            # we assign a default port
            port = 80
            webserver = temp[:webserverCheck]
        else:
            # else we need a specific port
            port = int((temp[(portCheck+1):])[:webserverCheck-portCheck-1])
            webserver = temp[:portCheck]

        try:
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.settimeout(config['CONNECTION_TIMEOUT'])
            s.connect((webserver,port))
            s.sendall(request)
            # we have to redirect the server's response to the client
            while 1:
                data = s.recv(config['MAX_REQUEST_LEN'])
                if (len(data)>0):
                    connection.send(data)
                else:
                    print("no connection sent to the client")
                    break
            s.close()
            connection.close()
        except socket.error as error_msg:
            print("ERROR OCCURED: ", clientAddress, error_msg)
            if s:
                s.close()
            if connection:
                connection.close()

    def getClient(self, clientAddress):
        return "ClientAddr"

    def shutdown(self):
        # exit the system
        self.serverSocket.close()
        sys.exit(0)