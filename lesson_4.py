# # Вывести на экран число "10" 20 раз столбиком.
# n = 10
# for i in range(20):
#     i = n
#     print(i)

# # Даны два числа a и b. Составить программу вывода на экран всех чисел от a до b.
# a = 2
# b = 7
# for i in range(a, b + 1):
#     print(i, end=' ')

# # Дано число N. Составить программу выводящую кубы чисел от 1 до N в одну строку.
# n = 20
# for i in range(1, n + 1):
#     print(i ** 3, end=' ')

# # Выведите на экран в одну строку числа от 100 до -100 включительно.
# for i in range(100, - 102, -1):
#     print(i, end=' ')

# Необходимо вывести все четные числа на отрезке [a; a * 10]
# a = 2
# for i in range(a, a * 10 + 1):
#     if i % 2 == 0:
#         print(i, end=' ')

# # Найти сумму всех целых чисел от 100 до 500 включительно.
# summa = 0
# for i in range(100, 501):
#     summa += i
# print(summa)

# # Найти произведение всех целых чисел от 5 до 20 включительно.
# multiply  = 1
# for i in range(5, 20):
#     multiply *= i
# print(multiply)

# # Дано натуральное число n. Вывести на экран факториал этого числа.
# n = int(input('Введите число n: '))
# factorial = 1
# if n > 0:
#     for i in range(1, n + 1):
#         factorial *= i
#     print('factorial = ',factorial)
# else:
#     print('Введите положительное число')

# Дан текст. Слова в тексте разделены одним или несколькими пробелами.
# # # Написать программу определяющую количество слов, заканчивающихся одной и той же буквой
# s = 'asd sdfnsjkb asda sad sd ss'
# s1 = ''
# s2 = ''
# count = 0
# for i in range(len(s)):
#     if s[i]!=' ':
#         s1 += s[i]
#     elif s[i] == " ":
#         if s1[-1] not in s2:
#             count += 1
#         s1 = ""
# print(count)
# # Вывести строку, удалив из нее повторные вхождения символов.
# s = 'abcddcdr'
# s1 = ''
# for i in range(len(s)):
#     if s[i] not in s1:
#         s1 += s[i]
# print(s1)

# # Дана строка символов, состоящая из произвольных натуральных чисел, разделенных пробелами.
# # Вывести четные числа этой строки.
# s = '123 45 23 87 345 56 2 981'
# s1 =''
# for i in range(len(s)):
#     if s[i]!=' ':
#         s1 += s[i]
#     elif s[i] == " ":
#         if s1.isdigit() and int(s1) % 2 == 0:
#             print(s1)
#         s1 = ""
# if int(s1) % 2 == 0:
#     print(s1)
# Узнав, что ДНК не является случайной строкой, только что поступившие в Институт биоинформатики студенты группы информатиков предложили использовать алгоритм сжатия, который сжимает повторяющиеся символы в строке. Кодирование осуществляется следующим образом:
# s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых символов исходной строки заменяются на этот символ и количество его повторений в этой позиции строки. Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом и выводит закодированную последовательность на стандартный вывод. Кодирование должно учитывать регистр символов.
# s = 'Aaaabbcaa'
# count = 0
# s1 = [1]
# s2 = ''
#
#
# print(s2)


# Sample Input 1:
# Aaaabbcaa
# Sample Output 1:
# a4b2c1a2
# Sample Input 2:
# Abc
# Sample Output 2:

