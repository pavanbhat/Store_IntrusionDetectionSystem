

class INTO:

    def __init__(self):
        self.table = ""
        self.attributes = []
        self.valuesCount = 0
        self.corrupted = False

    def parse(self, data):
        data = data.split()
        if data[0].upper() != 'INTO':
            self.corrupted = True
            return

        # extract table name
        for char in data[1]:
            if char == '(':
                break
            self.table += char

        self.attributes.append(data[1].replace(self.table, ""))
        for i in range(2, len(data)):
            if ')' in data[i]:
                break
            self.attributes.append(data[i].replace(',', '').strip())

        # validate the values part of SQL statement
        


    def __eq__(self, other):
        return (set(self.attributes) == set(other.attributes)) \
                and (self.table == other.table) \
                and not self.corrupted