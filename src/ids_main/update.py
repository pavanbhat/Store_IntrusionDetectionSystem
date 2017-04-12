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

        if query[2].upper() != 'SET':
            return False

        index = 3
        setData = ""
        while index < len(query) and query[index].upper() != 'WHERE':
            setData += query[index] + " "
            index += 1
        self.set[setIndex].parse(setData.strip())

        # parsing WHERE data
        # TODO handle nested statements for WHERE
        index += 1
        whereData = ""
        while index < len(query):
            whereData += query[index] + " "
            index += 1
        self.set[setIndex].poplateWhere(whereData)

    def __eq__(self, other):
        for curr in self.set:
            if curr in other.set:
                return True
        return False
