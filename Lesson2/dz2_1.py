if __name__ == '__main__':
    class ItemDiscount:
        def __init__(self, name, price):
            self.name = name
            self.price = price

    class ItemDiscountReport(ItemDiscount):
        def get_parent_data(self):
            return f'Наименование: {self.name}, цена: {self.price}'

    disc1 = ItemDiscountReport('Монитор', 15000)
    print(disc1.get_parent_data())
