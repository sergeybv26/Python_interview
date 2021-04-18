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

        zipped_str = list(zip(str_list, digit_list))

        for i in range(0, len(zipped_str), 3):
            zipped_str[i] = ('exmpl123',)

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
        with open(file, 'r', encoding='UTF-8') as f:
            file_dump = f.read()

        file_list = file_dump.split('\n')
        for line in file_list:
            count += 1
            if re.match('^exmpl123', line):
                print(f'Первое вхождение найдено в строке № {count}: {line}')
                break
        count = 0
        entry_list = []
        for line in file_list:
            count += 1
            if re.match('^exmpl123', line):
                entry_list.append(str(count))
                file_list[count - 1] = ' new987 '
        print(f'Вхождения найдены в строках: {", ".join(entry_list)}')

        with open(file, 'w', encoding='UTF-8') as f:
            for el in  file_list:
                f.write(''.join(el) + '\n')

        with open(file, 'r', encoding='UTF-8') as f:
            for line in f:
                if re.match('^\s?\w+\s?\n$', line):
                    print(line, end='')
        return None

    file_operation('dz3_5.txt')
