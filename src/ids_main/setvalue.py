from where import WHERE
import re

class SETvalue:

    def __init__(self):
        self.WHERE = []
        self.attributes = []

    def parse(self, query):
        queryData = re.split('and | or | AND | OR', query)
        for conditions in queryData:
            rvalue, lvalue = re.split('<|>|=| = | > | <', conditions)
            self.attributes.append(rvalue)


    def setTable(self, table):
        self.table = table

    def poplateWhere(self, whereData):
        self.WHERE.append(WHERE())
        self.WHERE[len(self.WHERE)-1].parse(whereData.strip())

    def __eq__(self, other):
        for where in self.WHERE:
            if where not in other.WHERE:
                return False
        return self.table == other.table \
                and set(self.attributes) == set(other.attributes)