# All imports here
from ProductList import ProductList, user_db


class ConnectionToDatabase:
    def make_connection(self, store, list_of_products=None):
        user_db.create_all(bind=['products'])
        if list_of_products != None:
            for i in list_of_products:
                product = i.split(',')
                print(product)
                enter_product = ProductList(uid=product[0], name=product[1], price=product[2], category=product[3])
                user_db.session.add(enter_product)
                user_db.session.commit()
        self.printIfExecuted(list_of_products)

    def printIfExecuted(self, list_of_products):
        print("Queried the following products to the database")
        for i in list_of_products:
            print(i)

#
# def main():
#     create_conn = ConnectionToDatabase()
#     create_conn.make_connection()


# if __name__ == '__main__':
#     main()

# # Getting data by their colummn names
# cur2 = conn.cursor(cursor_factory=ex.DictCursor)
# cur2.execute("select * from products")
#
# for i in rows:
#     print(i["userid"])
#
# # inputting data in a file
# fhandle= open('dataExport','w')
# cur3 = conn.cursor()
# cur3.copy_to('fhandle', 'products', sep=",")
#
# # inputting data from a file
# fhandle= open('dataExport','r')
# cur3 = conn.cursor()
# cur3.copy_to('fhandle', 'products', sep=",")
# cur3.commit()


