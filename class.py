# s = "concatenate"
# print(s[3:6])
# print(s[::2])
# print(s[7:])
# print(s[7:4:-1])
# print(s[::-1])
# s = 'hello'
# s = "H" + s[1:]
# print(s)
# поэлементный перебор строки
s = 'hello world'
# for elem in s:
#     print(elem)
# i = 0,1,2..len(s)
# по индексам перебор строки
# for i in range(len(s)):
#     print(s[i])
# in (в) not int (не в)
# if "H" in s:
#     print("yes")
# else:
#     print("no")
#    01234567
# s = "12a"
# s1 = 'helw'
# print(len(s))# длина строки
# print(s.find("hll"))
# print(s.rfind("h"))
# print(s.index('hll'))
# print(s.rindex('h'))
# print(s.islower())
# print(s.isupper())
# s = s.lower()
# s = s.upper()
# print(s.isalpha())
# print(s.isalnum())
# print(s.isdigit())
# if s.isdigit():
#     number = int(s)
#     print(number)

# s = s.replace("H","d")
# print(s.count("w"))
# s = s.swapcase()
# s = s.title()
# s = s.capitalize()
# print(s.startswith("hd"))
# print(s.endswith("sa"))
# print(s)
# print(ord(s))
# s = "hello"
# number = 10
# print("this is string:",s,"number is:",number)
# # %d - int %f -float %c - cисвол %s - str
# print("this is string: {} number is: {}".format(s,number))
# print(f"this is string: {s.upper()} number is: {number*3}")
# форматирование строк2
# f - строки
#Вывести строку, удалив из нее повторные вхождения символов.
# s = "hello world" #helo wrd
# s1 = "" # пустая строка
# for elem in s:
#     if elem not in s1:
#         s1 = s1 + elem
# print(s1)
# 23.  Определить число вхождений в строку подстроки 'abс'.
# Вывести символы строки, не являющиеся буквами или цифрами.
# s = 'dasabc 78asg1*!&abcSAdjas 12?'
# print(s.count("abc"))
# for elem in s:
#     if not elem.isdigit() and not elem.isalpha():
#         print(elem)
#-----кортежи
# n = int(input())
# while n > 99:
#     n = n // 10
# print(n%10)
# # Даны два кортежа:
# A = (13, 5, 43, 49, 67, 32, 12, 98, 6, 10, 34, 20, 55, 68, 14, 60, 14)
# B = (53, 21, 4, 23, 76, 3, 43, 12, 54, 342, 21)
# # Необходимо определить:
# # 1) Сумма элементов какого из кортежей больше и вывести соответствующее
# # сообщение на экран ( Сумма больше в кортеже - ..)
# # 2) Вывести на экран порядковые номера минимальных элементов этих
# # кортежей
# print("Сумма больше в кортеже -", 'A' if sum(A) > sum(B) else 'B')
# print(A.index(min(A)), B.index(min(B)))

# # Создайте  кортеж с цифрами от 0 до 9 и посчитайте сумму
# print(sum(tuple(range(0,10))))
# # Выведите статистику частности букв в кортеже
# long_word = ('т', 'т', 'а', 'и', 'и', 'а', 'и','и', 'и', 'т', 'т', 'а', 'и', 'и','и', 'и', 'и', 'т', 'и')
# a = long_word.count('т')
# b = long_word.count('а')
# c = long_word.count('и')
# print(f'Букв "т" {round((a * 100 / len(long_word)), 1)} %, букв "и" {round((c * 100 / len(long_word)), 1)} %,  букв "а" {round((b * 100 / len(long_word)), 1)} %')

#  Допишите скрипт для расчета средней температуры
# # Постарайтесь посчитать количество дней на основе week_temp.
# # Так наш скрипт сможет работать c данными за любой период
#
# week_temp = (26, 29, 34, 32, 28, 26, 23)
# sum_temp = sum(week_temp)
# days =len(week_temp)
# mean_temp = sum_temp / days
# print(int(mean_temp))