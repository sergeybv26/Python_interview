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

    class ItemDiscountReport1(ItemDiscount):

        def get_info(self):
            return f'Наименование: {self.name}'

    class ItemDiscountReport2(ItemDiscount):

        def get_info(self):
            return f'Цена: {self.price}'

    el1 = ItemDiscountReport1('Монитор', 15000)
    el2 = ItemDiscountReport2('Монитор', 15000)

    print(el1.get_info())
    print(el2.get_info())

    for el in (el1, el2):
        print(el.get_info())

    def get_name_price(el):
        print(el.get_info())

    get_name_price(el1)
    get_name_price(el2)
