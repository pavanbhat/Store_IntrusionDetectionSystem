import random
for i in range(0):
    print()
    q1 = "SELECT * from customers;"
    q2 = "INSERT INTO COMPANY(ID, NAME, AGE, ADDRESS, SALARY, JOIN_DATE) VALUES(1, 'Paul', 32, 'California', 20000.00, '2001-07-13');"
    q3 = "INSERT INTO COMPANY(ID, NAME, AGE, ADDRESS, SALARY, JOIN_DATE) VALUES(1, 'Paul', 32, 'California', 20000.00, '2001-07-13');"

Queries = {
    0: "SELECT",
    1: "INSERT",
    2: "CREATE",
    3: "DROP",
    4: "UPDATE",
    5: "DELETE"
}
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

Products = {
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

for i in range(11):
    print(Products[int(random.uniform(0, 10))], end=" ")