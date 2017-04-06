class Keyword:

    def __init__(self):
        self.setKey(key)

    # initialize_keywords creates hashmap of all SQL keywords
    # Class variable keyword is populated with all the data.
    def initialize_keywords(self):
        self.keyword = dict()

        self.keyword['SELECT'] = False
        self.keyword['INSERT'] = False
        self.keyword['CREATE'] = False
        self.keyword['DROP'] = False
        self.keyword['UPDATE'] = False
        self.keyword['DELETE'] = False
        self.keyword['TRUNCATE'] = False

    def getKeyword(self):
        return self.key

    def validKeyword(self):
        return self.key in keyword

    def setKey(self, key):
        self.key = key
