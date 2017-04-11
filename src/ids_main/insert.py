###

###

from into import INTO

class INSERT:

    def __init__(self):
        self.INTO = []

    def parse(self, data):
        data = data.split()

        # invalid query or currently not supported
        if data[0].upper() != 'INSERT':
            return

        # pass the other data to INTO for further parsing
        if data[1].upper() != 'INTO':
            return
        self.INTO.append(INTO())
        self.INTO[-1].parse(" ".join(data[1:]))

    def __eq__(self, other):
        for into in self.INTO:
            if into in other.INTO:
                return True
        return False