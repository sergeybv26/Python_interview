if __name__ == '__main__':
    from functools import reduce

    def multiplication_table(a, b):
        """
        :param a: первый множитель таблицы умножения
        :param b: второй множитель таблицы умножения
        :return: возвращает таблицу умножения размерностью А х В в виде строки
        """

        table_list = []
        for i in range(1, a + 1):
            for k in range(1, b + 1):
                table_list.append(f'{i} * {k} = {i * k}')

        table_str = reduce(lambda el1, el2: el1 + '\n' + el2, table_list)
        return table_str

    print(multiplication_table(2, 9))
