if __name__ == '__main__':

    import random
    import re

    def file_operation(file_name):
        """
        Создает текстовый файл.
        Генерирует два списка с числами и текстом
        Записыавет построчно в файл число и текст из списков
        :return:
        """

        digit_list = [str(random.randint(-10, 10)) for _ in range(10)]
        str_list = [(chr(random.randint(65, 90)) + chr(random.randint(97, 122))) for _ in range(10)]

        for i in range(0, len(str_list), 3):
            str_list[i] = 'exmpl123'

        zipped_str = zip(str_list, digit_list)

        try:
            with open(file_name, 'x', encoding='UTF-8') as f:
                for el in zipped_str:
                    f.write(' '.join(el) + '\n')
        except FileExistsError:
            print('Файл с таким именем уже существует')

        file_print(file_name)

        return None

    def file_print(file):
        """
        Выводит построчно содержимое файла
        :param file: ссылка на файл
        :return:
        """
        count = 0
        with open(file, 'a+', encoding='UTF-8') as f:
            for line in f:
                if re.match('^exmpl123', line) and count == 0:
                    print(f'Первое вхождение найдено в строке: {line}', end='')

                print(f'Вхождения найдены в строках: {line}', end='')
                count += 1
                f.write('new_str')

        return None

    file_operation('dz3_5.txt')
