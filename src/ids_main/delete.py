from ids_main.From import FROM

class DELETE():

    def __init__(self):
        self.FROM = []
        self.corrupted = False
        # Keyword.__init__('SELECT')


    # DELETE
    # FROM table_name
    # WHERE condition;
    def parse(self, query):
        print "select parse:"
        print "query:", query
        query = query.split()

        # Parsing columns
        index = 1
        fromIndex = 0 if len(self.FROM) == 0 else len(self.FROM)-1

        if query[index] != "FROM":
            self.corrupted = True
            return
        else:
            self.FROM.append(FROM())

        # parsing FROM data
        # TODO handle nested statements in FROM
        index += 1
        fromData = ""
        fromIndex = 0 if len(self.FROM) == 0 else len(self.FROM) - 1
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
            if curr in other.FROM:
                print "MATCHED"
                return True
        print "NOT MATCHED"
        return False
