from keywords import Keyword

class TrainTemplate:

    def __init__(self):
        self.template = dict()

    def train(self, fileName):
        with open(fileName) as f:
            data = f.read().split("\n")

        keyword = Keyword()
        for query in data:
            if len(query.split()) == 0:
                continue
            key = query.split()[0].upper()
            if key in self.template:
                self.template[key].parse(query)
            else:
                self.template[key] = keyword.getKeyword(key)
                self.template[key].parse(query)

    def getTemplate(self):
        return self.template