if __name__ == '__main__':
    import os
    import os.path

    def print_directory_contents(sPath):
        """
        :param sPath: В функцую передается имя каталога
        :return: Распечатывает содержимое каталога
        """

        list_dir = os.listdir(sPath)
        directory = []
        for el in list_dir:
            if os.path.isdir(f'/{sPath}/{el}'):
                for el_dir in os.