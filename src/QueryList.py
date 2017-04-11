class QueryList:
    __slots__ = 'list_of_queries'

    def __init__(self):
        list_of_queries = []

    def get_list_of_queries(self):
        return self.list_of_queries

    def add_query(self, query, product, table):
        if query.upper() == "SELECT" and table:
            query = "SELECT * from " + table + " WHERE id=" + product.pid + " and category=" + product.category + ";"
        elif query.upper() == "INSERT" and table:
            query = "INSERT INTO products(id, name, price, category) VALUES(1, 'Google Nexus', 650, 'Mobile');"
        elif query.upper() == "DELETE":
            query = "DELETE FROM " + table + " WHERE id=" + product.pid + ";"
        self.list_of_queries.append(query)

    def remove_query(self, query, product, table):
        if query.upper() == "SELECT" and table:
            query = "SELECT * from " + table + " WHERE id=" + product.pid + " and category=" + product.category + ";"
        elif query.upper() == "INSERT" and table:
            query = "INSERT INTO products(id, name, price, category) VALUES(1, 'Google Nexus', 650, 'Mobile');"
        elif query.upper() == "DELETE":
            query = "DELETE FROM " + table + " WHERE id=" + product.pid + ";"
        self.list_of_queries.append(query)
