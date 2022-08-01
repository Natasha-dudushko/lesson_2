# numb = int(input('Введите число: '))
# if numb % 10 == 3:
#     print('True')
# else:
#     print('False')
#
# a, b, c = map(int, input('Введите три числа:').split())
# if a < 0 or b < 0 or c < 0:
#     print('True')
# else:
#     print('False')
#
# # Задача 3
# n, k = map(int, input('Введите два целых числа:').split())
# if n != 0 and k != 0:
#     if n % 2 == k % 2:
#         print('числа n и k имеют одинаковую четность')
#     else:
#         print('числа n и k разной четности')
# else:
#     print('введите числа не равные 0')
#
# x = int(input('Введите число x:'))
# if x % 3 == 0 and x % 10 == 5:
#     print('True')
# else:
#     print('False')
#
a, b, c = map(int, input('Ведите три числа: ').split())
if a != 0 and b != 0 and c != 0:
    if a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
        print('3 четных числа')
    elif a % 2 == 0 and b % 2 == 0 or a % 2 == 0 and c % 2 == 0 or b % 2 == 0 and c % 2 == 0:
        print("2 четных числа")
    elif a % 2 == 0 or b % 2 == 0 or c % 2 == 0:
        print('1 четное число')
    else:
        print('0 четных чисел')
else:
    print('Введите числа не равные 0')
#
# a = int(input('Введите двухзначное число: '))
# if 1 <= a // 10 <= 9:
#     if a // 10 + a % 10 >= 10:
#         print("Да")
#     else:
#         print('Нет')
# else:
#     print('Вы ввели не двухзначное число')
#
# year = int(input('Введите год: '))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print('Висоскосный')
# else:
#     print('Не високосный')
#
# a = True
# b = False
# c = False
#
# T = a and not(b and not c)
# print(T)
# S = a and not(b) or (a and c)
# print(S)
# if T==S:
#     print('True')
# else:
#     print('Fars')
#
# x1, y1 = map(int, input("введите координаты первой клетки ").split())
# x2, y2 = map(int, input("введите координаты второй клетки ").split())
# if 1 <= x1 <= 8 and 1 <= x2 <= 8 and 1 <= y1 <= 8 and 1 <= y2 <= 8:
#     if (x1 + y1) % 2 == (x2 + y2) % 2:
#         print("клетки поля одного цвета")
#     else:
#         print('клетки поля разного цвета')
#
# else:
#     print("не корректно введены координаты фигур")
#
# x1, y1 = map(int, input("введите координаты ферзя ").split())
# x2, y2 = map(int, input("введите координаты фигуры ").split())
# if 1 <= x1 <= 8 and 1 <= x2 <= 8 and 1 <= y1 <= 8 and 1 <= y2 <= 8:
#     if x1 == x2 and y1 == y2:
#         print('Фигуры находятся на одном поле')
#     elif x1 == x2 or y1 == y2 or x1 + y1 == x2 + y2 or x1 - y1 == x2 - y2:
#         print("Ферзь угрожает Вашей фигуре")
#     else:
#         print('Ферзь не угрожвет Вашей фигуре')
# else:
#     print("не корректно введены координаты фигур")
#
# x1, y1 = map(int, input("введите координаты ладьи ").split())
# x2, y2 = map(int, input("введите координаты пешки ").split())
# if 1 <= x1 <= 8 and 1 <= x2 <= 8 and 1 <= y1 <= 8 and 1 <= y2 <= 8:
#     if x1 == x2 and y1 == y2:
#         print("Фигуры находятся на одном поле")
#     elif x1 == x2 or y1 == y2:
#         print('Ладья бьет пешку')
#     elif (x1 == x2 - 1 or x1 == x2 + 1) and (y1 == y2 + 1 or y1 == y2 - 1):
#         print('Пешка бьет ладью')
#     else:
#         print('Фигурам ничего не угрожает')
# else:
#     print("не корректно введены координаты фигур")
#
# x1, y1 = map(int, input("введите координаты слона ").split())
# x2, y2 = map(int, input("введите координаты коня ").split())
# if 1 <= x1 <= 8 and 1 <= x2 <= 8 and 1 <= y1 <= 8 and 1 <= y2 <= 8:
#     if x1 == x2 and y1 == y2:
#         print('Фигуры находятся на одном поле')
#     elif x1 + y1 == x2 + y2 or x1 - y1 == x2 - y2:
#         print("Слон бьет коня")
#     elif (x1 == x2 - 1 or x1 == x2 - 2 or x1 == x2 + 1 or x1 == x2 + 2) and (
#             y1 == y2 + 2 or y1 == y2 + 1 or y1 == y2 - 1 or y1 == y2 - 2):
#         print('Конь бьет слона')
#     else:
#         print('Фигурам ничего не угрожает')
# else:
#     print("не корректно введены координаты фигур")

# #Задача 7
# numb = int(input('Введите четырехзначное число: '))
# if 1 <= numb // 1000 <= 9:
#     if numb % 1111 == 0:
#         print('Все цифры в нем одинаковы')
#     else:
#         print('Цифры в нем не одинаковы')
# else:
#     print('Вы ввели не четырехзначное число')

