from keywords import Keyword

class TrainTemplate:

    def __init__(self):
        self.template = dict()
        self.keyword = Keyword()

    def train(self, fileName):
        with open(fileName) as f:
            data = f.read().split("\n")


        for query in data:
            if len(query.split()) == 0 and self.queryPrevTrained(query):
                continue
            key = query.split()[0].upper()
            if key in self.template:
                self.template[key].parse(query)
            else:
                self.template[key] = self.keyword.getKeyword(key)
                self.template[key].parse(query)

    def queryPrevTrained(self, query):
        key = query.split()[0].upper()
        queryTemplate = self.keyword.getKeyword(key)
        queryTemplate.parse(query)

        return queryTemplate == self.template['DELETE']

    def getTemplate(self):
        return self.template