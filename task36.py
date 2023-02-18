""" Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
ровно два аргумента, как, например, у операции умножения.

Ввод: 
print_operation_table(lambda x, y: x * y)
Вывод:
 1 2 3 4 5 6
 2 4 6 8 10 12
 3 6 9 12 15 18
 4 8 12 16 20 24
 5 10 15 20 25 30
 6 12 18 24 30 36  """

row_set = 1
col_set = 1

def f(table_set,index_row=2,index_col=2):
    print(table_set[index_row-1][index_col-1])
    #return table_set[row-1][col-1]

def print_operation_table(operation,num_rows=6,num_columns=6):
    table = []
    rows_list=[]
    operation=f
    for row in range(num_rows):
        rows_list.clear()
        for col in range(1,num_columns+1):
            rows_list.append(col+row)
        table.append(rows_list)
        print(rows_list,end='\n')
    operation(table,row_set,col_set)

table=[[10,20,30],[40,50,60]]
print_operation_table(f(table,1,1),3,3) 
