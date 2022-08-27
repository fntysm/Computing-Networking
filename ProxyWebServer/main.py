import sockets
from sockets import Server
config = {
    'HOST_NAME': 'localhost',
    'BIND_PORT': 12345,
    'MAX_REQUEST_LEN': 4096,
    'CONNECTION_TIMEOUT' : 10
}


if __name__ == "__main__":
    server = Server(config)
    server.clientListen()

