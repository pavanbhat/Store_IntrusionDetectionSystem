class ListOfProducts:
    __slots__ = 'data_send'

    def __init__(self):
        self.data_send = []

    def get_data(self):
        return self.data_send

    def set_data(self, product):
        self.data_send.append(product)

    def remove_data(self, product_id):
        if len(self.data_send) > 0:
            for i in range(len(self.data_send)):
                if self.data_send[i].pid == product_id:
                    del self.data_send[i]
                    break
