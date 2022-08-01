# # 1. Создать текстовый файл и записать в него 6 строк.
# # Записываемые строки вводятся с клавиатуры.
# f = open('test.txt', 'w', encoding='utf-8')
# f.write('Я помню чудное мгновенье:' + '\n')
# f.write('Передо мной явилась ты!' + '\n')
# f.write('Как мимолетное виденье,' + '\n')
# f.write('Как гений чистой красоты!' + '\n')
# f.write('В томленьях грусти безнадежной,' + '\n')
# f.write('В тревогах шумной суеты,'  + '\n')
# f.close()


# # 2. В конец существующего текстового файла записать три новые
# # строки текста. Записываемые строки вводятся с клавиатуры.
# f = open('test.txt', 'a', encoding='utf-8')
# f.write('Звучал мне долго голос нежный' + '\n')
# f.write('И снились милые черты.' + '\n')
# f.close()
#
# # 3. Дан текстовый файл. Подсчитать количество символов в нем. Без \n
# f = open('test.txt', 'r', encoding='utf-8')
# lst = f.readlines()
# f.close()
# s = 0
# for elem in lst:
#     s += len(elem.rstrip())
# print(s)
# # 4.Имеется текстовый файл, содержащий 5 строк. Переписать каждую из его строк в список в том же порядке.
# lst = []
# f = open('test.txt', 'r+', encoding='utf-8')
# for i in range(5):
#     elem = f.readline().rstrip()
#     lst.append(elem)
# print(lst)
# f.close()
#
# # 5. Имеется текстовый файл. Получить текст, в котором в конце каждой строки из заданного файла
# # добавлен восклицательный знак.
# f = open('test.txt', 'r', encoding='utf-8')
# s = f.readlines()
# f.close()
# for elem in s:
#     elem = elem.rstrip()
#     if elem[-1] == '!':
#         print(elem)
#
# # 6. Имеется текстовый файл.
# # -Найти длину самой длинной строки.
# # -Найти номер самой длинной строки. Если таких строк несколько, то найти номер одной из них.
# # -Напечатать самую длинную строку. Если таких строк несколько, то напечатать первую из них.
# f = open('test.txt', 'r', encoding='utf-8')
# s = f.readlines()
# f.close()
# lst = list(elem.rstrip() for elem in s)
# d = {len(el): el for el in lst}
# print(max(d))
# print(lst.index(d[max(d)]))
# print(d[max(d)])
#
# # 7. Создать файл input.txt и записать в него 10 чисел через пробел. Считать из него эти числа.
# # Затем записать их произведение в файл output.txt.
# import random
# lst = [str(random.randint(1,20)) for i in range(10)]
# s = ' '.join(lst)
# f = open('input.txt', 'w', encoding='utf-8')
# f.write(s)
# f.close()
# f = open('input.txt', 'r', encoding='utf-8')
# lst1 = f.readline().rstrip().split()
# lst1 = list(map(int, lst1))
# total = 1
# for num in lst1:
#     total *= num
# f.close()
# f = open('output.txt', 'w', encoding='utf-8')
# f.write(str(total))
# f.close()
#
# # 8. Имеется текстовый файл. Все четные строки этого файла записать во второй файл,
# # а нечетные — в третий файл. Порядок следования строк сохраняется.
# f = open('test.txt', 'r', encoding='utf-8')
# lst = f.readlines()
# d = {i + 1: lst[i] for i in range(len(lst))}
# lst1 = [value for key, value in d.items() if key % 2 != 0]
# lst2 = [value for key, value in d.items() if key % 2 == 0]
# s1 = ''.join(lst1)
# s2 = ''.join(lst2)
# f.close()
# f = open('test1.txt', 'w', encoding='utf-8')
# f.write(s1)
# f.close()
# f = open('test2.txt', 'w', encoding='utf-8')
# f.write(s2)
# f.close()
#
# # 9. Имеются два текстовых файла с одинаковым числом строк. Выяснить, совпадают ли их строки.
# # Если нет, то получить номер первой строки, в которой эти файлы отличаются друг от друга.
# with open('test.txt', 'r', encoding='utf-8') as f_test:
#     lst1 = f_test.readlines()
# with open('test1.txt', 'r', encoding='utf-8')  as f_test1:
#     lst2 = f_test1.readlines()
#
# for i in range(len(lst1)):
#     for j in range(len(lst2)):
#         if lst1[i] != lst2[j] and i == j:
#             print(f'Отличаются в {i + 1} строке')
#             break
# # 10.В справочной аэропорта хранится расписание вылета самолетов на следующие сутки.
# # Для каждого рейса указаны номер рейса, пункт назначения, время вылета.
# # Вывести все номера рейсов и время вылета самолета для заданного пункта назначения.
# with open('spravka.txt', 'w', encoding='utf-8') as f:
#     f.write('725 Москва 13:25' + '\n')
#     f.write('346 Минск 22:13' + '\n')
#     f.write('123 Берлин 09:00' + '\n')
#
# city = {}
# with open('spravka.txt', 'r', encoding='utf-8') as f_sp:
#     for line in f_sp:
#         a, b, c = line.rstrip().split()
#         city[b] = [a, c]
# for key, value in city.items():
#     print(key, *value)
#
# # 11. Ведомость студентов, сдававших сессию, содержит ФИО и оценки по четырем предметам.
# # Вывести список студентов, сдавших сессию со средним баллом больше 7.
# with open('test.txt', 'w', encoding='utf-8') as f:
#     f.write('Иванов Иван Иванович 7 9 7 8' + '\n')
#     f.write('Петров Петр Петрович 5 7 6 9' + '\n')
#     f.write('Краснов Глеб Романович 9 10 7 8' + '\n')
#
# student = {}
# with open('test.txt', 'r', encoding='utf-8') as f_stud:
#     for line in f_stud:
#         line = line.rstrip().split()
#         key = ' '.join(line[0:3])
#         value = line[3:]
#         value = list(map(int, value))
#         student[key] = value
#
# for key, value in student.items():
#     if sum(value) / len(value) > 7:
#         print(key)
# # 12. В файле записаны в столбик целые числа. Отсортировать их по возрастанию суммы цифр
# # и записать в другой файл.
# # 61
# # 8
# # 45
# # 10
# # File output:
# # 10 61 8 45
# with open('test.txt', 'w', encoding='utf-8') as f:
#     f.write('61' + '\n')
#     f.write('8' + '\n')
#     f.write('45' +'\n')
#     f.write('10' + '\n')
# d = {}
#
# with open('test.txt', 'r', encoding='utf-8') as f_sum:
#     for line in f_sum:
#         line = line.rstrip()
#         key = int(line)
#         for i in line:
#             d[key] = d.get(key, 0) + int(i)
# for value in sorted(d.values()):
#     for key in d:
#         if d[key] == value:
#             print(key, end=' ')
#             break
# # 13. Вашей задачей будет восстановление исходной строки обратно. Напишите программу, которая считывает
# # из файла строку, соответствующую тексту, сжатому с помощью кодирования повторов, и производит обратную
# # операцию, получая исходный текст. Для решение вам необходимо открыть файл для чтения 13.txt
# # Sample Input:
# # a3b4c2e10b1
# # Sample Output:
# # aaabbbbcceeeeeeeeeeb
# with open('13.txt', 'r', encoding='utf-8') as f:
#     s = f.read()
#
# lst_alpha = []
# for i in range(len(s) - 1):
#     if s[i].isalpha():
#         lst_alpha.append(s[i])
# print(lst_alpha)
# lst_num = []
# s1 = ''
# for i in range(len(s)):
#     if s[i].isdigit():
#         s1 += s[i]
#     elif not s[i].isdigit() and len(s1) >= 1:
#         lst_num.append(s1)
#         s1 = ''
# print(lst_num)
# s_total = ''
# for i in range(len(lst_alpha)):
#     for j in range(len(lst_num)):
#         if i == j:
#             s_total += lst_alpha[i] * int(lst_num[i])
#             break
# print(s_total)
# with open('13.txt', 'a', encoding='utf-8') as f_rez:
#     f_rez.write(s_total)
