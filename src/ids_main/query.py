###

Single SQL query parsed data

###

class Query():


    def __init__(self, query):
        self.type = {"SELECT" : 0,
                    "INSERT" : 1,
                    "CREATE" : 2,
                    "DROP" : 3,
                    "UPDATE" : 4,
                    "DELETE" : 5,
                    "TRUNCATE" : 6]}
        parse(query)

    ###
    setter function sets the type of SQL query by checking the map hashmap
    ###
    def setType(self, type):
        typeNum = self.type[type]


    ###
    getter fuction returns the transaction ID.
    ###
    def getTransactionID(self, id):
        return self.id


    ###
    TODO

    Parser the sql query and updates the class variables.
    ###
    def parse(self, query):
        query, self.id = query.split(";")

        query = query.split(" ")
        setType(query[0])

        # Parse other attributes
