from ids_main.select import SELECT
from ids_main.insert import INSERT

class Template:

    def __init__(self):
        self.template = dict()

    def train(self, fileName):
        print "template train"
        with file(fileName) as f:
            data = f.read().split("\n")

        for query in data:
            if len(query.split()) == 0:
                continue
            key = query.split()[0].upper()
            if key in self.template:
                self.template[key].parse(query)
            elif key == 'SELECT':
                self.template['SELECT'] = SELECT()
            elif key == 'INSERT':
                self.template['INSERT'] = INSERT()
            # elif key == 'UPDATE':
            #     self.template['SELECT'] = UPDATE()
            # elif key == 'DELETE':
            #     self.template['SELECT'] = DELETE()
            self.template[key].parse(query)

    def checkMatch(self, query):
        print "template match:"
        print "query", query
        temp = INSERT()
        temp.parse(query)
        print "result ", temp == self.template['INSERT']
