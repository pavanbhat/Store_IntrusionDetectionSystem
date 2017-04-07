from ids_main.From import FROM

class SELECT():

    def __init__(self):
        self.FROM = []
        # Keyword.__init__('SELECT')


    # SELECT column1, column2, ...
    # FROM table_name
    # WHERE condition;
    def parse(self, query):
        print "select parse:"
        print "query:", query
        query = query.split()

        # Parsing columns
        index = 1
        fromIndex = 0 if len(self.FROM) == 0 else len(self.FROM)-1
        column = []
        while query[index] != 'FROM':
            column.append(query[index])
            index += 1
        self.FROM.append(FROM())
        self.FROM[fromIndex].setColumn([column])

        print "column:", column

        # parsing FROM data
        # TODO handle nested statements in FROM
        index += 1
        fromData = ""
        while query[index] != 'WHERE' and index < len(query):
            fromData += query[index] + " "
            index += 1
        self.FROM[fromIndex].parse(fromData.strip())
        print "from data: ", fromData

        # parsing WHERE data
        # TODO handle nested statements for WHERE
        index += 1
        whereData = ""
        while index < len(query):
            whereData += query[index] + " "
            index += 1
        self.FROM[fromIndex].poplateWhere(whereData)
        print "where data:", whereData


    # Overriding = comparator
    def __eq__(self, other):
        # check for matching FROM nodes
        for curr in self.FROM:
            if curr == other.FROM[0]:
                print "MATCHED"
                return True
        print "NOT MATCHED"
        return False
