if __name__ == '__main__':
    class ItemDiscount:
        def __init__(self, name, price):
            self.__name = name
            self.__price = price

        def set_price(self, price):
            self.__price = price

        @property
        def name(self):
            return self.__name

        @property
        def price(self):
            return self.__price

    class ItemDiscountReport(ItemDiscount):

        def __init__(self, name, price, discount):
            super().__init__(name, price)
            self.discount = discount

        def get_parent_data(self):
            return f'Наименование: {self.name}, цена: {self.price}'

        def __str__(self):
            return f'Цена товара со скидкой: {self.price - self.price * self.discount / 100}'

    disc1 = ItemDiscountReport('Монитор', 15000, 10)
    print(disc1.get_parent_data())
    print(disc1)
