if __name__ == '__main__':

    import random

    def file_operation(file_name):
        """
        Создает текстовый файл.
        Генерирует два списка с числами и текстом
        Записыавет построчно в файл число и текст из списков
        :return:
        """

        digit_list = [str(random.randint(-10, 10)) for _ in range(10)]
        str_list = [(chr(random.randint(65, 90)) + chr(random.randint(97, 122))) for _ in range(10)]

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
        with open(file, 'r', encoding='UTF-8') as f:
            for line in f:
                print(line, end='')

        return None

    file_operation('dz3_4.txt')
