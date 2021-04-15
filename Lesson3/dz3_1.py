if __name__ == '__main__':

    import os

    def name_file(full_file_name):
        """
        Осуществляет поиск полного пути по имени файла,
        а затем «выделение» из этого пути имени файла (без расширения)
        :param full_file_name: имя файла с расширением
        :return:имя файла без расширения
        """
        path_file = os.path.abspath(full_file_name)
        name_full = os.path.basename(path_file)

        return os.path.splitext(name_full)[0]

    print(name_file('find_file.txt'))
