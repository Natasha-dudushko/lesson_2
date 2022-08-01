# # 1.	Сгенерировать двумерный список. Среди строк заданной матрицы, содержащих только нечетные элементы,
# # найти строку с максимальной по модулю суммой элементов.
# lst = [[1, 1, 3], [3, 5, 3], [2, 4, 8]]
# max_sum = 0
# for i in range(len(lst)):
#     count = 0
#     summa = 0
#     for j in range(len(lst[i])):
#         if lst[i][j] % 2 == 1:
#             count += 1
#             summa += abs(lst[i][j])
#     if count == len(lst[i]) and summa > max_sum:
#         max_sum = summa
# print(max_sum)
#
#
# # 2.	Дано нечетное число n. Создайте двумерный список из n×n элементов, заполнив его символами "."
# # (каждый элемент списка является строкой из одного символа). Затем заполните символами "*" среднюю строку списка,
# # средний столбец массива, главную диагональ и побочную диагональ. В результате  в списке должна получиться снежинка.
# # Выведите полученный список на экран, разделяя элементы списка пробелами.
# import math
# n = int(input('Введите нечетное число: '))
# lst = [['.' for i in range(n)] for j in range(n)]
# for i in range(len(lst)):
#     if i == math.floor(n / 2):
#         lst[i] = ['*'] * n
#     for j in range(len(lst[i])):
#         if i == j:
#             lst[i][j] = '*'
#         elif i + j == n - 1:
#             lst[i][j] = '*'
#         elif j == math.floor(n / 2):
#             lst[i][j] = '*'
# for elem in lst:
#     print(*elem)
#
# # 3.	Даны два числа n и m. Создайте двумерный список размером n×m и заполните его символами "." и "*" в шахматном порядке.
# # В левом верхнем углу должна стоять точка.
# n, m = map(int,input('Введите размеры матрицы: ').split())
# lst = [['.' if (i + j) % 2 == 0 else '*' for i in range(1, n + 1)] for j in range(1, m + 1)]
# for elem in lst:
#     print(*elem)
#
# # 4. Сгенерируйте список как показано ниже
# n = int(input())
# lst = [[i * j for j in range(n)] for i in range(n)]
# for i in range(n):
#     for j in range(n):
#         if i == 0 or j == 0:
#             lst[i][j] = 1
# for elem in lst:
#     print(*elem)
#
# # Задача № 5
# n, m = map(int,input('Введите размеры матрицы: ').split())
# lst = [[j ** i for j in range(1, n + 1)] for i in range(1, m + 1)]
# for elem in lst:
#     print(*elem)
#
# # Задача № 6
# import random
# n = int(input())
# lst = [[random.randint(1,10) for i in range(n)] for j in range(n)]
# for elem in range(n):
#     if str(elem) == str(elem)[::-1]:
#         print('YES')
#         break
# else:
#     print('NO')
# # Разработать программу, запрашивающую у пользователя матрицу размером M x N.
# # Выполнить поворот ее на 90° против часовой стрелки . Размерность матрицы  задаётся случайными значениями.
# # Результаты вывести на консоль.
# # Sample Input:
# # 2 1 2 1
# # 1 3 3 1
# # 2 3 4 5
# # Sample Output:
# # 1 1 5
# # 2 3 4
# # 1 3 3
# # 2 1 2
# m, n = int(input()), int(input())
# lst = [[2, 1, 2, 1], [1, 3, 3, 1], [2, 3, 4, 5]]
# lst1 = [elem[::-1] for elem in lst]
# for j in range(n):
#     for i in range(m):
#         print(lst1[i][j], end=' ')
#     print()
# # Выведите таблицу размером n×n, заполненную числами от 1 до n*n “змейкой”, выходящей из
# # левого верхнего угла, как показано в примере (здесь n=5):
# n = int(input())
# lst = [[j + n * i for j in range(1, n + 1)] for i in range(n)]
# for i in range(n):
#     if i % 2 == 0:
#         print(*lst[i])
#     else:
#         lst[i] = lst[i][::-1]
#         print(*lst[i])
