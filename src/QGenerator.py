# All imports here
import random

class QGenerator:
        '''
        A class that assists in auto-generating queries for the template generator
        '''

        # Number of queries that need to be generated
        num = 0

        def __init__(self, num):
            '''
            Parameterized constructor for taking the number of queries to be generated as input
            :param num: Number of queries to be generated
            '''
            self.num = num

        # Types of queries that can be generated for the choice of products
        Queries = {
            0: "SELECT",
            1: "INSERT",
            # 2: "CREATE",
            # 2: "DROP",
            # 3: "UPDATE",
            # 4: "DELETE",
            # 5: "TRUNCATE"
        }

        # List of Dummy Names that can be used with their
        Names = {
            0: "Pavan",
            1: "Yogeesh",
            2: "Alankar",
            3: "Tim",
            4: "Andy",
            5: "Robert",
            6: "Anna",
            7: "Cindy",
            8: "Nona",
            9: "Vandy",
            10: "Dilan"
        }

        # A list of addresses a user can belong to
        UserAddress = {
            0: "California",
            1: "New York",
            2: "Arizona",
            3: "Ohio",
            4: "Washington",
            5: "Texas",
            6: "Philadelphia",
            7: "New Jersey",
            8: "Georgia",
            9: "Florida",
            10: "Vermont",
            11: "Massachusetts"
        }

        # A list of categories an user can choose from
        Category = {
            0: "Mobile Phone",
            1: "Laptop",
            2: "Computer Mouse",
            3: "Keyboard",
            4: "Kindle",
            5: "Book",
            6: "CD",
            7: "Headphones",
            8: "Bag",
            9: "Watch",
            10: "Shoe"
        }

        # A user's id which can be used as a foreign key
        userid = 1000

        def generateQueries(self):
            '''
            A method that generates queries randomly.
            :return: None
            '''
            # increase the range to generate however many queries are required to be generated
            for id in range(self.num):
                # generates a random query
                query = int(random.uniform(0, 2)) # Changes to be made here

                if query == 0:
                    print('SELECT * from products where category = "' + self.Category[int(random.uniform(0, 10))] \
                          + '" and id = ' + str(self.userid) + ';', end=" \n")
                    self.userid += 1
                elif query == 1:
                    print('INSERT INTO products(id, name, price, category) VALUES(' + str(self.userid) \
                          + ", '" + (self.Names[int(random.uniform(0, 10))] + str(id)) \
                          + "', " + str(round(random.uniform(0, 1000), 2)) + ', \'' \
                          + ', \'' + self.Category[int(random.uniform(0, 10))] + '\');', end=" \n")
                    self.userid += 1
                elif query == 2:
                    print('SELECT * from products where category = "' + self.Category[int(random.uniform(0, 10))] + '"', end=" ")
                elif query == 3:
                    print('SELECT * from products where category = "' + self.Category[int(random.uniform(0, 10))] + '"', end=" ")
                elif query == 4:
                    print('SELECT * from products where category = "' + self.Category[int(random.uniform(0, 10))] + '"', end=" ")
                else:
                    print('SELECT * from products where category = "' + self.Category[int(random.uniform(0, 10))] + '"', end=" ")

def main():
    '''
    The main program
    :return: None
    '''
    while True:
        num = input('Please enter the number of queries that need to be generated: (Eg: 10)')
        if num.isdigit():
            break

    num = int(num)
    # Object of class QGenerator
    qGen = QGenerator(num)

    # Starts the random query generation
    qGen.generateQueries()


if __name__ == '__main__':
    main()