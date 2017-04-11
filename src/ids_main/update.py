from setvalue import SETvalue

class UPDATE:

    def __init__(self):
        self.set = []

    def parse(self, query):
        query = query.split()

        if query[0] != 'UPDATE':
            return False

        index = 1
        self.set.append(SETvalue())
        setIndex = 0 if len(self.set) == 0 else len(self.set)-1

        if len(query) < 2:
            return False
        self.set[setIndex].setTable(query[1])
        while query !=