""" 
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной 

Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
для изменения и удаления данных."""


import os
from data_create import name_data, surname_data, adress_data, phone_data,id_data


file_name = 'data.txt'
id_last=0


def print_data():

    if os.path.exists(file_name):
        print('Вывод данных из фала: ')
        with open(file_name,'r',encoding='utf-8') as file:
            data_list = file.readlines()
            for element in data_list:
             print(element)
    else:
       print('Записей нет')

def input_data():
  str_ID=''  
  ##### ID ####
  if os.path.exists(file_name):
    with open(file_name,'r',encoding='utf-8') as file:
      row_list = file.readlines()
      for ch in row_list[-1]:
          if ch == ';':
              id_last = int(str_ID)            
              break
          str_ID+=ch
  else:   
    id_last=0
    ############

  print('Введите данные для записи в файл: ')
  id_last=id_data(id_last)
  name=name_data()
  surname=surname_data()
  phone=phone_data()
  adress=adress_data()

  with open(file_name,'a',encoding='utf-8') as file:
    file.write(f'{id_last};{name};{surname};{phone};{adress} \n')
    
def filter_data(filter_string):
    with open(file_name,'r',encoding='utf-8') as file:
      list_data = file.readlines()

      if ';' in filter_string:
        list_filter = filter_string.split(';')
      else:
        list_filter=[filter_string]

      iSfind=False
      for element in list_data:
        temp_record = element.split(';')
        count=0
        for record in temp_record:           
            for element_filter in list_filter:
                if element_filter.lower() in record.lower() and len(element_filter)==len(record):
                    count+=1
        if count == len(list_filter):
            print(element)
            iSfind=True
    if not iSfind:
      print('Записей не найдено!')        
               
def сhange_data():
  num_rec = input('Введите номер записи для изменения: ')
  with open(file_name, 'r', encoding='utf-8') as file:
    ptr=0
    i=0
    row_list = file.readlines()
    for row in row_list:
        if num_rec in row:           
            ptr=i
        i+=1 
    with open(file_name, 'w', encoding='utf-8') as file:
        i=0
        for row in row_list:
            if i == ptr:
                print(f'Вы хотите изменить запись:  {row}')
                print('Введите данные для записи в файл: ')
                name=name_data()
                surname=surname_data()
                phone=phone_data()
                adress=adress_data()
                file.write(f'{num_rec};{name};{surname};{phone};{adress} \n')
            else:
               file.write(row)
            i+=1

def delete_data():
  num_rec = input('Введите номер записи для удаления: ')
  with open(file_name, 'r', encoding='utf-8') as file:
    ptr=0
    i=0
    row_list = file.readlines()
    for row in row_list:
        if num_rec in row:           
            ptr=i
        i+=1 
    with open(file_name, 'w', encoding='utf-8') as file:
        i=0
        for row in row_list:
            if i == ptr:
                print(f'Удалено:  {row}')
            else:
               file.write(row)
            i+=1

     
         
   


