import socket


class ConnectToIDS:
    __slots__ = 'host', 'port'

    def __init__(self):
        '''
        Default constructor that initializes the host and port for establishing a connection to IDS.
        '''
        self.host = '127.0.0.1'
        self.port = 5555

    def connect_to_ids(self, host='129.21.115.185', port=8000):
        '''
        
        :param host: IP address of the IDS 
        :param port: port number to connect to the IDS from
        :return: None
        '''
        sock = socket.socket()
        sock.connect((host, port))
        print("Sending query to IDS...")
        message = input("->")
        while message != 'q':
            message1 = bytearray(message, "ascii")
            sock.send(message1)
            message = input("->")
        sock.close()

def main():
    '''
    This is the main function that starts the connection with IDS
    :return: None
    '''
    connect = ConnectToIDS()
    connect.connect_to_ids()


if __name__ == '__main__':
    main()
