
# # 1.	Дан кортеж. Вывести все его совершенные числа. 6 = 1 + 2 + 3
# # 28 = 1 + 2 +4 + 7 +14
#
# tup = (2, 3, 4, 5, 6)
# print(tup)
# for elem in tup:
#     summa = 0
#     for i in range(1, elem):
#         if elem % i == 0:
#             summa += i
#     if elem == summa:
#         print(elem, end=' ')
#
# # 2.	Элементы кортежа числа и строки. Все строки в кортеже сделать перевёртышами а числа умножить на два.
# tup = (12, 'asdf', 13, 'asef')
# lst = []
# for elem in tup:
#     if type(elem) == int:
#         lst.append(elem * 2)
#     elif type(elem) == str:
#         lst.append(elem[::-1])
# print(lst)
#
# # 3.	Дан кортеж. Найти разность между его максимальным и минимальный элементом.
# import random
# tup = tuple(random.randint(1,10) for i in range(7))
# print(tup)
# print(max(tup) - min(tup))
#
# # 4.	Ввести список с клавиатуры. Список преобразовать в кортеж.
# # Посчитать количество элементов между максимальным и минимальным. (5,2,8,9,6,8,3,4) 1 элемент
# tup = tuple(list(map(int, input().split())))
# a = tup.index(min(tup))
# b = tup.index(max(tup))
# print(len(tup[a+1: b]) if a < b else len(tup[b+1: a]))
#
# # 5.	Дан кортеж. Написать программу, определяющую сколько раз менялся знак в кортеже. (5,2,-2,7,-8,-9,1) 4 раза
# tup = (5, 2, -2, 7, -8, -9, 1)
# count = 0
# for i in range(len(tup) - 1):
#     if tup[i] > 0 and tup[i+1] < 0 or (tup[i] < 0 and tup[i+1] > 0):
#         count += 1
# print(count)
#
# # 6.	Дан кортеж. Вывести на экран все простые числа в данном кортеже.
# tup = tuple(list(map(int, input().split())))
# for i in range(len(tup)):
#     count = 0
#     for j in range(1, i +1):
#         if i % j == 0:
#             count += 1
#     if count == 2:
#         print(i, end=' ')
#
# # 7.	Дан кортеж. Посчитать сумму элементов между максимальным и минимальным не включая эти элементы. (1,5,2,8,9,6,8,3,4) sum= 15
# tup = tuple(list(map(int, input().split())))
# a = tup.index(min(tup))
# b = tup.index(max(tup))
# print(sum(tup[a+1: b]) if a < b else sum(tup[b+1: a]))
#
#
# # 9.	Дан кортеж. Без функций и дополнительных списков вывести все повторяющиеся элементы. (count не использовать).
# tup = (1, 3, 2, 3, 1, 4, 2, 5, 2)
# for i in range(len(tup)):
#     tap1 = tup[i + 1:]
#     if tup[i] in tap1:
#         print(tup[i],end=' ')
# product = {
#     "melon": [200, 6.22],
#     "water": [500, 5.52],
#     "apple": [100, 6.21],
#     "cheese": [5, 52.52],
#     'butter': [20, 3.61]
# }
# summa = 0
# while True:
#     name_product = input("enter name product or exit:")
#     if name_product == "exit":
#         break
#     if name_product in product:
#         print('yes')
#         quantity_product = int(input('enter quantity product:'))
#         if quantity_product <= product[name_product][0]:
#             summa += quantity_product * product[name_product][1]
#             product[name_product][1] -= quantity_product
#         else:
#             print(f'quantity product: {product[name_product][0]}')
#     else:
#         print(f"no product name {name_product}")
#
# print(summa)