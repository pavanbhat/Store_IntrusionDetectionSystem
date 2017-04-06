import re

class WHERE:

    def __init__(self):
        self.attributes = []

    def parse(self, queryData):
        print "where parse:", queryData
        # TODO
        # Detect multiple select statement and handle

        # no nested statments, so multiple conditions
        self.queryData = queryData
        queryData = re.split('and | or | AND | OR', queryData)

        for conditions in queryData:
            rvalue, lvalue = re.split('<|>|=| = | > | <', conditions)
            self.attributes.append(rvalue)

    # Overriding = comparator
    def __eq__(self, other):
        return set(self.attributes) == set(other.attributes)
