class QueryList:
    '''
    
    '''
    __slots__ = 'list_of_queries'

    def __init__(self):
        '''
        
        '''
        self.list_of_queries = []

    def get_list_of_queries(self):
        '''
        
        :return: 
        '''
        return self.list_of_queries

    def add_query(self, query, product=None, table=""):
        '''
        
        :param query: 
        :param product: 
        :param table: 
        :return: 
        '''
        if query.upper() == "SELECT" and table != "":
            query = "SELECT * from " + table + " WHERE id=" + product.pid + " and category=" + product.category + ";"
        elif query.upper() == "INSERT" and table != "":
            query = "INSERT INTO " + table + "(id, name, price, category) VALUES(" + product.pid + ",'" + product.name + "'," + product.price + ",'" + product.category + "');"
        elif query.upper() == "DELETE" and table == "":
            query = "DELETE FROM cart WHERE product_id=" + product + ";"
        elif query.upper() == "DELETE" and table != "":
            query = "DELETE FROM " + table + " WHERE product_id=" + product + ";"
        print(self.get_list_of_queries())
        self.list_of_queries.append(str(query))

    def remove_query(self, query, product, table):
        '''
        
        :param query: 
        :param product: 
        :param table: 
        :return: 
        '''
        if query.upper() == "SELECT" and table:
            query = "SELECT * from " + table + " WHERE id=" + product.pid + " and category=" + product.category + ";"
        elif query.upper() == "INSERT" and table:
            query = "INSERT INTO products(id, name, price, category) VALUES(1, 'Google Nexus', 650, 'Mobile');"
        elif query.upper() == "DELETE":
            query = "DELETE FROM " + table + " WHERE id=" + product.pid + ";"
        self.list_of_queries.append(query)
