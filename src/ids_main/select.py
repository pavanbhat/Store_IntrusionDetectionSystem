class Select:

    def __init__(self):
        Keyword.__init__('SELECT')
        self.column = []
        self.FROM = None
        self.WHERE = None

    # SELECT column1, column2, ...
    # FROM table_name
    # WHERE condition;
    def parse(self, query):
        query = query.split()

        # Parsing columns
        index = 0
        while query[index] != 'FROM':
            self.column.append(query[index])
            index += 1

        # parsing FROM data
        # TODO handle nested statements in FROM
        index += 1
        fromData = ""
        while query[index] != 'WHERE':
            fromData += query[index] + " "
        self.FROM = From()
        self.FROM.parse(fromData.strip())

        # parsing WHERE data
        # TODO handle nested statements for WHERE
        index += 1
        whereData = ""
        while query[index] != 'WHERE':
            fromData += query[index] + " "
        self.WHERE = Where(whereData)

    # Overriding = comparator
    def __eq__(self, other):
        if set(self.column) != set(other.column):
            return False
        #check FROM and WHERE data are same
        if (self.FROM == other.FROM) and \
            (self.WHERE == other.WHERE):
            return True
        return False
