# # С клавиатуры вводится 7 значное число. Если четных цифр в нем больше, чем
# # нечетных, то найти сумму всех его цифр, если нечетных больше, то найти
# # произведение 1 3 и 6 цифры.
# n = int(input('enter number: '))
# count1 = 0 #счетчик четных
# count2 = 0 #счетчик нечетных
# total = 0
# s = str(n)
# while n > 0:
#     total += n % 10
#     if n % 10 % 2 == 0:
#         count1 += 1
#     elif n % 10 % 2 == 1:
#         count2 += 1
#     n //= 10
# if count1 > count2:
#     print(total)
# else:
#     print(int(s[0]) * int(s[2]) * int(s[5]))


# # С клавиатуры вводится текст, определить, сколько в нём гласных, а сколько
# # согласных. В случае равенства вывести на экран все гласные буквы
# s1 = input('Введите строку: ')
# s = s1.lower()
# count_g = 0
# count_s = 0
# s3 = ''
# for i in range(len(s)):
#     if s[i] in 'aeiouy':
#         count_g += 1
#         s3 += s[i]
#     if s[i] in 'bcdfghjklmnpqrstvwxz':
#         count_s += 1
# if count_g == count_s:
#     print(s3)

# # Вводится 2 числа с клавиатуры (от 1 до 20). Так же генерируется 2 числа рандомно.
# # Посчитать, сколько раз пара введенных чисел с клавиатуры окажется больше
# # рандомной пары. Проверку выполнить 7 раз.
# # В случае равенства (количества, когда пара больше и всех остальных случаем)
# # вывести случайные числа, полученные в 4 итерации
# import random
# a, b = map(int,input('Введите два числа: ').split())
# count_ab = 0
# count_cd = 0
# s1 = ''
# s2 = ''
# i = 1
# while i <= 7:
#     c = random.randint(1,100)
#     d = random.randint(1,100)
#     s1 += str(c) + ' '
#     s2 += str(d) + ' '
#     if a + b > c + d:
#         count_ab += 1
#     else:
#         count_cd +=1
#     i += 1
#
# if count_ab > count_cd:
#     print(count_ab)
# else:
#     s1 = s1.split()
#     s2 = s2.split()
#     print(s1[4], s2[4])

# # Посчитать, сколько раз встречается определенная цифра в числах. Количество
# # введенных чисел и искомая цифра задаются с клавиатуры. Числа выбираются
# # рандомно.
# import random
# n = int(input('Введите искомую цифру: '))
# k = int(input('Введите количество введенных чисел: '))
# count = 0
# while k != 0:
#     a = random.randint(1,100)
#     while a > 0:
#         if a % 10 == n:
#             count +=1
#         a //= 10
#     k -= 1
# print(count)

# # Вводится строка, содержащая буквы, целые неотрицательные числа и иные символы.
# # Требуется все числа, которые встречаются в строке отдельно вывести на экран. Строка
# # может содержать пробелы.
# s = '12mbnjv  ajdh32 123 kjkj3 44 2'
# s +=" "
# s1 =""
# for i in range(len(s)):
#     if s[i]!=' ':
#         s1 += s[i]
#     elif s[i] == " " and len(s1) >= 1:
#         if s1.isdigit():
#             print(s1, end=' ')
#         s1 = ""
# # Посчитать, сколько пар (стоят рядом) верхнего и нижнего регистра находится в
# # веденном с клавиатуры слове. (Пример HjkLM- 1 пара нижнего, 1 пара верхнего), а
# # также сколько всего букв в слове, сколько гласных и согласных.
# s = 'HjkLM'
# s += ' '
# count_l = 0
# count_up = 0
# for i in range(len(s) - 1):
#     if s[i].islower() and s[i+1].islower():
#         count_l += 1
#     elif s[i].isupper() and s[i+1].isupper():
#         count_up += 1
# print(f'{count_l} - пара нижнего, {count_up} - пара верхнего.')
# print(f'{len(s)} - количество букв в строке')
# s1 = s.lower()
# count_g = 0
# count_s = 0
# for i in range(len(s)):
#     if s[i] in 'aeiouy':
#         count_g += 1
#     if s[i] in 'bcdfghjklmnpqrstvwxz':
#         count_s += 1
# print(count_g, '- количество гласных')
# print(count_s, '- количество согласных')