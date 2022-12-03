# 1) Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


# Задача 1
# def sum_of_num():
#     number = [1, 3, 2, 4, 6, 4]
#     x=1
#     max=0
#     for i in number:
#         if x%2==0:    #т.к x изначально был задан 1, нечетные числа будут стоять под четными x
#             max+=i
#         x+=1
#     print(max)
# sum_of_num()


# 2) Написать программу, которая генерирует двумерный массив на A x B элементов ( A и B вводим с клавиатуры)
# И считаем средне-арифметическое каждой строки (не пользуемся встроенными методами подсчета суммы)
#Задача 2
# from random import randint
# def gen_mass_2():
#     n = int(input("Ведите высоту массива: "))
#     m = int(input("Ведите ширину массива: "))
#     list = [[randint(1, 10) for j in range(m)] for i in range(n)]
#     print (list)
    

#     max_1 = 0
#     for i in range(0, n):
#         for j in range(0,m):
#             max_1 = max_1 + list[i][j]
#     mas_sum = max_1/(n*m)
#     print(mas_sum)

# gen_mass_2()

#Задача 3
# 3) Сгенерируйте список на 30 элементов. Отсортируйте список по возрастанию, методом сортировки выбором.
# import random
# def gen_mass_30():
#     list_1 = []
#     for i in range(0,30):
#         list_1.append(random.randint(0,30))
#     print(list_1)
#     n=1
#     while n<len(list_1):
#         for i in range(len(list_1)-n):
#             if list_1[i] > list_1[i+1]:
#                 list_1[i],list_1[i+1] = list_1[i+1],list_1[i]
#         n+=1
#     print(list_1)
# gen_mass_30()
    


    