if __name__ == '__main__':

    user_number = input('Введите число: ')

    if user_number.find('.') == -1:
        print('Число целое')
    else:
        print('Число дробное')
        user_number_list = user_number.split('.')
        print(user_number_list[0] == user_number_list[1])