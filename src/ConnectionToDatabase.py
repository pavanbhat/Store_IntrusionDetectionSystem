# All imports here
import psycopg2 as pg
from flask_sqlalchemy import SQLAlchemy

import WebUI

WebUI.app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:@localhost/store'
db = SQLAlchemy(WebUI.app)


class ConnectionToDatabase:
    def make_connection(self, list_of_products=None):
        conn = pg.connect("dbname='postgres' user='postgres' password='secret' host='localhost'")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO products(id, name, price, category) VALUES(3, 'Red Dragon Mouse', 19, 'Mouse');")
        conn.commit()
        cursor.execute("select * from products")
        self.printIfExecuted(cursor)

    def printIfExecuted(self, cursor):
        rows = cursor.fetchall()
        for i in rows:
            print(i)


def main():
    create_conn = ConnectionToDatabase()
    create_conn.make_connection()


if __name__ == '__main__':
    main()

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


