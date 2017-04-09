from ids_main.select import SELECT
from ids_main.insert import INSERT
from ids_main.delete import DELETE
from ids_main.keywords import Keyword

class TrainTemplate:

    def __init__(self):
        self.template = dict()

    def train(self, fileName):
        print "template train"
        with file(fileName) as f:
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