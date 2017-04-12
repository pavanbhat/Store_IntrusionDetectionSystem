import socket

class ConnectToIDS:
    __slots__ = 'host', 'port', 'sock'

    def __init__(self):
        '''
        Default constructor that initializes the host and port for establishing a connection to IDS.
        '''
        self.host = input("Enter IDS hostname, Eg:127.0.0.1:")
        self.port = int(input("Enter IDS port number, Eg:8000:"))
        self.sock = None

    def connect_to_ids(self, message="None", queries=None):
        '''
        
        :param host: IP address of the IDS 
        :param port: port number to connect to the IDS from
        :return: None
        '''
        # if self.sock is None:
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))
        print("Sending queries to IDS...")
        flag = True
        while flag:
            message1 = bytearray(message, "ascii")
            self.sock.send(message1)
            data = self.sock.recv(1024)
            received_data = data.decode('ascii')
            if received_data is not None:
                break
        received_data = received_data.split(";")
        # print("obj data: ", obj)
        print(received_data)
        print("queries data: ", queries)
        success_queries = ""
        filtered_queries = ""
        insert_queries = ""

        received_data = received_data[:len(queries)]

        for check in range(len(received_data)):
            if received_data[check].__eq__(""):
                continue
            if "False" not in received_data:
                if received_data[check].__eq__("True") and queries[check].find("INSERT") != -1:
                    insert_queries += queries[check] + "\n"
                elif received_data[check].__eq__("True") and queries[check].find("INSERT") == -1:
                    success_queries += queries[check] + "\n"
            else:
                filtered_queries += queries[check] + "\n"

        print("Inserted queries: ", insert_queries)
        print("Success queries: ", success_queries)
        print("Filtered queries: ", filtered_queries)

        # self.sock.close()
        return success_queries, filtered_queries, insert_queries

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
