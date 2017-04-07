class Product:
    __slots__ = 'pid', 'name', 'price', 'category'

    def __init__(self, pid, name, price, category):
        self.pid = pid
        self.name = name
        self.price = price
        self.category = category

    def dump(self):
        return {"product": {"pid": self.pid,
                            "name": self.name,
                            "price": self.price,
                            "category": self.category}}
