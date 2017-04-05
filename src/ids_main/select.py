class Select:

    def __init__(self):
        Keyword.__init__('SELECT')
        self.FROM = []
        self.WHERE = None

    # SELECT column1, column2, ...
    # FROM table_name
    # WHERE condition;
    def parse(self, query):
        query = query.split()

        # Parsing columns
        index = 0
        fromIndex = size(self.FROM)
        column = []
        while query[index] != 'FROM':
            column.append(query[index])
            index += 1
        self.FORM[fromIndex].setColumn([column])

        # parsing FROM data
        # TODO handle nested statements in FROM
        index += 1
        fromData = ""
        while query[index] != 'WHERE':)
            fromData += query[index] + " "
        self.FROM.append(From())
        self.FROM[].parse(fromData.strip())

        # parsing WHERE data
        # TODO handle nested statements for WHERE
        index += 1
        whereData = ""
        while query[index] != 'WHERE':
            fromData += query[index] + " "
        self.FROM[fromIndex].populateWhere(whereData);


    # Overriding = comparator
    def __eq__(self, other):
        # check for matching FROM nodes
