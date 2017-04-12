# From class reponsible of parsing from data
from where import WHERE

class FROM:

    def __init__(self):
        self.table = ""
        self.WHERE = []
        self.column = []
        self.SELECT = None

    def parse(self, queryData):
        # TODO
        # Detect multiple select statement

        # no nested statments, so table name
        self.table = queryData.strip()

    def setColumn(self, column):
        self.column.extend(column)

    def poplateWhere(self, whereData):
        self.WHERE.append(WHERE())
        self.WHERE[len(self.WHERE)-1].parse(whereData.strip())

    # Overriding = comparator
    def __eq__(self, other):
        for where in self.WHERE:
            if where not in other.WHERE:
                return False
        return self.table == other.table \
                and set(self.column) == set(other.column)
