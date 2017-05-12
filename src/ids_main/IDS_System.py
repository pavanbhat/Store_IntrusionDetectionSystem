###
#
# Parser's the SQL query
#
###

import os
import socket

from dominate.tags import tr
from template_detect import MatchTemplate
from template_train import TrainTemplate


'''
Intrusion Detection System main controlling class
This class trains the system using train log file 
and detects the newly arriving transaction as malicious or not
'''
class IDS:


    '''
    This method initiates the IDS system
    '''
    def __init__(self):
        self.trainTemplate = TrainTemplate()
        self.template = None
        # Create a TCP/IP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    '''
    train method takes the path to the train transaction log.
    By default it takes the path as current directory and file
    "train.txt".
    '''
    def train(self, path="train.txt"):
        if not os.path.exists(path):
            print("Training file not found!")
            return False
        self.trainTemplate.train(path)
        self.template = self.trainTemplate.getTemplate()
        return True

    ###
    # detect method takes the query which is to be checked with the system trained
    # previously. This passes the query to matching with the template, if the match is found
    # then it is malicious so it returns True else False
    ###
    def detect(self, query="SELECT * from products WHERE id=0 and category=Laptop"):
        if self.template is None:
            print("Template is not trained, please train the template first. Thanks!")
            return False
        self.matchTemplate = MatchTemplate(self.template)
        return self.matchTemplate.checkMatch(query)


    ###
    # Listens at a perticular port listening to for the connection
    # from the user end of the applicationself.
    # Binds to port 9999
    #
    # saves the connection in self.app and the server address in self.appAddr
    ###
    def connectToApplication(self):
        try:
            # Bind the socket to the port
            self.appIP = str(input("Enter Application IP address: "))
            self.appPort = int(input("Enter Application port number: "))
            self.sock.bind((self.appIP, self.appPort))

            print("Successfull connected to application")
        except Exception as e:
            print("Connection failed")
            print("ERROR:", str(e))
            return False
        return True

    ###
    # Receives upto 2048 bytes of data from the client application.
    # Any SQL query wont be more than 2048 bytes.
    ###
    def recvParse(self):
        print("waiting for connection")
        self.sock.listen(15)
        self.app, self.appAddr = self.sock.accept()

        queries = ""
        while True:
            tempQuery = self.app.recv(1024)
            if not tempQuery:
                break
            queries += tempQuery.decode('utf-8')
            if len(tempQuery) != 1024:
                break
        if len(queries) > 0: print(queries.split(';'))
        return queries.split(';')

    def sendToApp(self, data):
        print("Sending result back to application")
        print("result: ", data)
        self.app.send(bytes(data, 'ascii'))

    ###
    # callQueryNode function passes the query to the query parser.
    # This class parsers the query and updates it the form of node.
    # Which could be further used to create template
    ###
    def callQueryNode(self, query):
        #parse query
        #query = Query(query)
        pass

    ###
    # this method connects to the IDS and starts the IDS
    ###
    def run(self):
        validConnection = False
        while not validConnection:
            print("Connecting to Application")
            validConnection = ids.connectToApplication()
            print("Attempt failed, trying again!")

        self.start()

    ###
    # start method starts the IDS.
    # Receives the query which should be checked
    # and saves the result and sends back to the application.
    ###
    def start(self):
        self.train()

        while True:
            transactionQueries = self.recvParse()

            # handling empty checkout
            if len(transactionQueries) == 1 and transactionQueries[0] == '':
                self.sendToApp("False")
                continue

            result = ""
            for query in transactionQueries:
                if query == '':
                    continue
                if not self.detect(query):
                    result += "False;"
                else:
                    result += "True;"
            self.sendToApp(result)


if __name__ == '__main__':
    ids = IDS()
    # ids.train()
    # ids.detect()
    ids.connectToApplication()
    ids.start()