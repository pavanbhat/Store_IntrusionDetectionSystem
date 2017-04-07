

class INTO:

    def __init__(self):
        self.table = ""
        self.attributes = []
        self.valuesCount = 0
        self.corrupted = False

    def parse(self, data):
        print "INTO"
        data = data.split()
        if data[0].upper() != 'INTO':
            self.corrupted = True
            return

        # extract table name
        for char in data[1]:
            if char == '(':
                break
            self.table += char

        print "table name: ", self.table

        self.attributes.append(data[1].replace(self.table, ""))
        for attribute in data[2:]:
            if ')' in attribute:
                break
            self.attributes.append(attribute.replace(',', '').strip())

        print "attributes: ", self.attributes

        # validate the values part of SQL statement
        


    def __eq__(self, other):
        return (set(self.attributes) == set(other.attributes)) \
                and not self.corrupted