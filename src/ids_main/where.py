import re

class From:

    def __init__(self, queryData):
        self.queryData = queryData
        self.attributes = []

    def parse(queryData = self.queryData):
        # TODO
        # Detect multiple select statement and handle

        # no nested statments, so multiple conditions
        queryData = re.split('and | or | AND | OR')

        for conditions in queryData:
            rvalue, lvalue = re.split('<|>|=| = | > | <')
            attributes.append(rvalue)

    # Overriding = comparator
    def __eq__(self, other):
        return set(self.attributes) == set(other.attributes)
