# # Выведите все четные элементы списка. При этом используйте цикл for, перебирающий элементы списка, а не их индексы!
# lst = [123, 432, 34, 2, 1, 6, 87, 107]
# for num in lst:
#     if num % 2 == 0:
#         print(num, end=' ')
# # Задано два списка. Найти наименьшие среди элементов первого списка, которые не входят во второй список.
# lst1 = [12, 4, 65, 4, 3, 103]
# lst2 = [9, 0, -3, 3, 23]
# lst1.sort()
# for min_lst1 in lst1:
#     if min_lst1 not in lst2:
#         print(min_lst1)
#         break
# # Задан список из k чисел. Определить количество инверсий в списке
# # (т. е. таких пар элементов, в которых большее число находится слева от меньшего).
# k = int(input('enter number: '))
# lst = []
# for i in range(k):
#     lst.append(int(input()))
# count = 0
# for i in range(len(lst)-1):
#     if lst[i] > lst[i + 1]:
#        count += 1
# print(count)
#
# # Программе подаётся на вход произвольная строка. Удалите из нее повторяющиеся символы
# # (т. е. символы, встречающиеся в строке во второй или более раз)
# # и выведите результат на экран. Задачу решить через список. Функцию set не использовать
# # Sample Input 1:
# # Ха-ха-ха-ха
# # Sample Output 1:
# # Ха-х
# lst = list(input('Введите строку: '))
# lst1 = []
# for elem in lst:
#     if elem not in lst1:
#         lst1.append(elem)
# print(*lst1, sep='')
#
# # Дан список положительных целых чисел .
# # Вставить после каждого чётного числа его перевёртыш. 18 81, 42 24, 8 8, 122 221
# lst = [12, 13, 204, 105]
# for i in range(len(lst)):
#     if lst[i] % 2 == 0:
#         a = str(lst[i])
#         b = int(a[::-1])
#         lst.insert(i + 1, b)
#     else:
#         continue
# print(*lst)

# lst1 = []
# a = 0
# for elem in lst:
#     if elem % 2 != 0:
#         lst1.append(elem)
#     elif elem % 2 == 0:
#         a = str(elem)[::-1]
#         lst1.append(elem)
#         lst1.append(int(a))
# print(*lst1, sep=' ')
#
# # Дан список . Вычислить сколько раз в нем встречается каждый элемент, не используя сортировки.
# lst = list('12aaab132')
# lst1 = []
# for elem in lst:
#     if elem not in lst1:
#         lst1.append(elem)
#         print(f'{elem} встречается {lst.count(elem)} раза')
#
# # Дан список . Перезаписать его так, чтобы сначала были все положительные числа,
# # а затем все отрицательные и нули, сохраняя порядок их следования.
# lst = [1, 23, -3, 0, -32, 3, 0]
# lst_negative = []
# lst_zero = []
# lst_positiv = []
# for num in lst:
#     if num < 0:
#         lst_negative.append(num)
#     elif num == 0:
#         lst_zero.append(num)
#     else:
#         lst_positiv.append(num)
# print(lst_positiv + lst_negative + lst_zero)
#
# # Дан список . Продублировать все неповторяющиеся элементы.
# lst = list('1233')
# lst1 = []
# for elem in lst:
#     if lst.count(elem) > 1:
#         lst1.append(elem)
#     elif lst.count(elem) == 1:
#         lst1.append(elem)
#         lst1.append(elem)
# print(*lst1, sep='')
#
# # задача №10
# s = ''
# lst = []
# lst_get = []
# while s != '.':
#     s = input()
#     if 'POST' in s:
#         s1 = s.split()
#         s1.remove('POST')
#         s2 = ' '.join(s1)
#         lst.append(s2)
#     elif 'DELETE' == s:
#         del lst[-1]
#     elif 'GET' == s:
#         lst_get.append(lst[-1])
#
# print(* lst_get, sep='\n')
# print(*lst)