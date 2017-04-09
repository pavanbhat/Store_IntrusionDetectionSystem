###
#
# Parser's the SQL query
#
###

import socket
import sys
import os
from template_train import Template


class IDS:

    def __init__(self):
        self.template = Template()

    def trainTemplate(self, path=""):
        path = os.getcwd() + "/train.txt"
        self.template.train(path)

    def detection(self):
        self.template.checkMatch("DELETE FROM carts WHERE id = 1;")

    ###
    # Listens at a perticular port listening to for the connection
    # from the user end of the applicationself.
    # Binds to port 9999
    #
    # saves the connection in self.app and the server address in self.appAddr
    ###
    def connectToApplication(self):
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to the port
        server = ('localhost', 9999)
        sock.bind(server)

        self.app, self.appAddr = sock.accept()


    ###
    # Receives upto 2048 bytes of data from the client application.
    # Any SQL query wont be more than 2048 bytes.
    ###
    def recvData(self):
        return self.app.recv(2048)


    ###
    # callQueryNode function passes the query to the query parser.
    # This class parsers the query and updates it the form of node.
    # Which could be further used to create template
    ###
    def callQueryNode(self, query):
        #parse query
        #query = Query(query)
        pass

if __name__ == '__main__':
    ids = IDS()
    ids.trainTemplate()
    ids.detection()