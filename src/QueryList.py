class QueryList:
    __slots__ = 'list_of_queries'

    def __init__(self):
        list_of_queries = []

    def get_list_of_queries(self):
        return self.list_of_queries

    def add_query(self, query):
        if query.upper() == "SELECT":

        elif query.upper() == "INSERT":

        elif query.upper() == "DELETE":
