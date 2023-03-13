""" Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и выводить на печать построчно последние строки в количестве lines (на всякий случай проверим, что задано положительное целое число). Протестируем функцию на файле «article.txt» со следующим содержимым:
Вечерело
Жужжали мухи
Светил фонарик
Кипела вода в чайнике
Венера зажглась на небе
Деревья шумели
Тучи разошлись
Листва зеленела """
import sys
import fileinput


def read_last(file, lines):
    i = 1
    if (lines > 0):
        with open(file, mode="r", encoding="utf-8") as f:
            line_count = sum(1 for line in open(file))
            for line in f.readlines():
                if (i > (line_count-lines)):
                    print(line)
                i = i+1
    else:
        print("Введите положительное число строк")

def findLen(str):
    counter = 0    
    for i in str:
        counter += 1
    return counter

def longest_words(file):
    wordsList = list()
    resultList=list()
    words =list()
    maxstr=1
    with open(file, mode="r", encoding="utf-8") as f:
        for line in f.readlines():
            wordsList.append(list(line.split('\n')[0].split(' ')))

        for lines in wordsList:
            for word in lines:
                words.append(word)
                if findLen(word) >= maxstr:
                    maxstr = findLen(word)        
        for word in words:
            if findLen(word) == maxstr:     
                resultList.append(word)
        print("Самые длинные слова: ")
        print(*resultList)
    with open(fileResult ,'w', encoding='utf-8') as file:
        for word in resultList:
            file.write(word+'\n')

filename = 'article.txt'
fileResult = 'result.txt'
linesNum = int(input("Введите количество строк: "))
read_last(filename, linesNum)
longest_words(filename)


    
