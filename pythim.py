# with open('test1.txt', 'w', encoding='utf-8') as f1:
#     f1.write('Президент США Дональд Трамп продолжил обмен выпадами с руководством КНДР. We all know why Joe Biden is rushing to falsely pose as the winner, and why his media allies are trying so hard to help him: they don’t want the truth to be exposed.' + '\n')
#     # f1.write('Simple is better than 1.' + '\n')
    # f1.write('Complex is better than complicated.' + '\n')


# count_letters = 0
# count_words = 0
# count_line = 0
# s1 = ''
# with open('lines.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         count_line += 1
#         for elem in line.rstrip():
#             if elem.isalpha():
#                 count_letters +=1
#                 s1 += elem
#             else:
#                 s1 += ' '
#
# print(f'{count_letters} letters')
# print(f'{len(s1.split())} words')
# print(f'{count_line} lines')

# with open('test.txt', 'r', encoding='utf-8') as f:
    # f.write('there are many different holidays on the first of january we celebrate new year on the seventh of january and the twenty-fifth of december we have christmas the twenty-third of february is the day of the defenders of the motherland or the army day then comes easter and radonitsa the first of may is the labour day the ninth of may is victory day the third of july is independence day then comes the seventh of november the day of the october revolution and so on' + '\n')
    #
    # d = {}
    # s = f.read().strip().split()
    # for elem in s:
    #     d[elem] = len(elem)
    # for key, value in d.items():
    #     if value == max(d.values()):
    #         print(key)
# with open('test1.txt', 'r') as f:
#     lst = f.readlines()
#     print(lst)
#     for i in range(len(lst)):
#         if lst[i][:3] == 'def ':
#             print(lst[i])
# total = 0
# for n in range(1, 11):
#     for k in range(1, 21):
#         for m in range(1, 201):
#             if 10*n+5*k+0.5*m==100:
#                 total += 1
#
#                 if n + m + k == 100:
#                     print('n =', n, 'k =', k, 'm =', m)
# print('Общее количество натуральных решений =', total)
# объявление функции
# def draw_triangle():
#     for i in range(10):
#         for j in range(i + 1):
#             print('*', end='')
#         print()
#
# draw_triangle()