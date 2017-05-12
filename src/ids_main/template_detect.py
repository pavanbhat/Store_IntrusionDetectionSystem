from keywords import Keyword

###
# MatchTemplate class checks if the new query is valid
# or not by looking at the model.
###
class MatchTemplate:

    def __init__(self, template):
        self.template = template

    def checkMatch(self, query):
        keyword = Keyword()

        if len(query.split()) == 0:
            return True

        key = query.split()[0].upper()
        queryTemplate = keyword.getKeyword(key)
        queryTemplate.parse(query)

        if key not in self.template:
            print("OOPS key not found")
            return False
        print("result ", queryTemplate == self.template[key])
        return queryTemplate == self.template[key]