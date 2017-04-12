import socket

class ConnectToIDS:
    __slots__ = 'host', 'port'

    def __init__(self):
        '''
        Default constructor that initializes the host and port for establishing a connection to IDS.
        '''
        self.host = '127.0.0.1'
        self.port = 5555

    def connect_to_ids(self, host='129.21.122.59', port=8000, message="None"):
        '''
        
        :param host: IP address of the IDS 
        :param port: port number to connect to the IDS from
        :return: None
        '''
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        print("Sending queries to IDS...")
        while message != 'q':
            message1 = bytearray(message, "ascii")
            sock.send(message1)
            # data = sock.recv(1024)
            message = input("->")

        received_data = message.split(";")
        # filtered_queries =
        # success_queries =
        # insert_queries =
        # for i in range(len(received_data)):
        #     if received_data[i] is True:
        #         list

        sock.close()

def main():
    '''
    This is the main function that starts the connection with IDS
    :return: None
    '''
    connect = ConnectToIDS()
    connect.connect_to_ids()


if __name__ == '__main__':
    # main()
    pass
