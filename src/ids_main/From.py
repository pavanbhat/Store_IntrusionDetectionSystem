# From class reponsible of parsing from data

class From:

    def __init__(self, queryData):
        self.queryData = queryData
        self.table = ""
        self.SELECT = None

    def parse(queryData):
        # TODO
        # Detect multiple select statement

        # no nested statments, so table name
        self.table = queryData.strip()
