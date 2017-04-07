from ids_main.select import SELECT

class Template:

    def __init__(self):
        self.template = dict()
        self.template['SELECT'] = SELECT()

    def train(self, fileName):
        print "template train"
        with file(fileName) as f:
            data = f.read().split(";")

        print data[0].split()
        for query in data:
            if len(query.split()) > 1 and query.split()[0].upper() == 'SELECT':
                self.template['SELECT'].parse(query)


    def templateMatch(self, query):
        print "template match:"
        print "query", query
        temp = SELECT()
        temp.parse(query)
        print "result ", temp == self.template['SELECT']
