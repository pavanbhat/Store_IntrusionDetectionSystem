from ids_main.select import SELECT


class Template:

    def __init__(self):
        self.template = dict()
        self.template['SELECT'] = SELECT()

    def train(self, fileName):
        print "template train"
        with file(fileName) as f:
            data = f.read().split("\n")

        for query in data:
            if len(query.split()) == 0:
                continue
            if query.split()[0].upper() == 'SELECT':
                self.template['SELECT'].parse(query)

    def checkMatch(self, query):
        print "template match:"
        print "query", query
        temp = SELECT()
        temp.parse(query)
        print "result ", temp == self.template['SELECT']
