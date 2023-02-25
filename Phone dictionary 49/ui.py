from logger import input_data, print_data, filter_data,delete_data, сhange_data

def interface():
    print('''Выберите режим работы: 
                                    1 - запись данных
                                    2 - вывод данных
                                    3 - поиск данных по параметрам
                                    4 - удалить запись данных
                                    5 - изменить запись данных
                                    ''')
    command=int(input())
    while command < 1 or command >5:
        print('Введите корректный номер команды')
        command=int(input())
    if command ==1:
        input_data()
    elif command==2:
        print_data()
    elif command==3:
        print('Введите параметры поиска через ; :')
        filter_string = input()
        filter_data(filter_string)
    elif command==4:
        delete_data()
    elif command==5:
        сhange_data()

     