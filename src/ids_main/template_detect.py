from ids_main.select import SELECT
from ids_main.insert import INSERT
from ids_main.delete import DELETE
from keywords import Keyword

class MatchTemplate():

    def __init__(self, template):
        self.template = template

    def checkMatch(self, query):
        keyword = Keyword()

        if len(query.split()) == 0:
            return True

        key = query.split()[0].upper()
        queryTemplate = keyword.getKeyword(key)
        queryTemplate.parse(query)

        print "template match:"
        print "query", query
        print "result ", queryTemplate == self.template['DELETE']