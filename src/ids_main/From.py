# From class reponsible of parsing from data

class From:

    def __init__(self, queryData):
        self.queryData = queryData
        self.table = ""
        self.WHERE = []
        self.column = []
        self.SELECT = None

    def parse(queryData = self.queryData):
        # TODO
        # Detect multiple select statement

        # no nested statments, so table name
        self.table = queryData.strip()

    def setColumn(self, column):
        self.column.append(column)

    def poplateWhere(self, wheredata):
        self.WHERE.append(WHERE(fromData.strip()))
        self.WHERE[size(self.WHERE)-1].parse()

    # Overriding = comparator
    def __eq__(self, other):
        return self.table == other.table
