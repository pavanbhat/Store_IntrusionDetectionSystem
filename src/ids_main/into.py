

class INTO:

    def __init__(self):
        self.table = ""
        self.attributes = []

    def parse(self, data):
        data = data.split()
        if data[0] ==