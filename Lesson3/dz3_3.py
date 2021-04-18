if __name__ == '__main__':

    keys = ['a', 'b', 'c', 'd', 'e', 'f']
    values = [1, 2, 3, 4]

    result_dict = {}

    for key in keys:
        try:
            result_dict[key] = values.pop(0)
        except IndexError:
            result_dict[key] = None

    print(result_dict)
