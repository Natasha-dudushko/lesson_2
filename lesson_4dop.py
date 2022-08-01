# С клавиатуры вводится натуральное число n <= 1000. Выведите n строк вида "На лугу n коров",
# склоняя слово "коров" в соответствии с числом n. Проверяем большие числа!!!

# n = int(input('enter n: '))
# for i in range(1, n + 1):
#         if i == 1 or i % 10 == 1:
#             print(f'На лугу {i} корова')
#         elif 2 <= i <= 4 or 2 <= i % 10 <= 4:
#             print(f'На лугу {i} коровы')
#         elif 5 <= i <= 9 or i % 10 == 0 or 5 <= i % 10 <= 9:
#             print(f'На лугу {i} коров')

# # Найти натуральное число из диапазона [n, m] (n, m – натуральные числа),
# # которое имеет наибольшее количество делителей.
# maxcount = 0
# maxn = 0
# n, m = map(int,input('Enter numbers ').split())
# for i in range(n, m + 1):
#     count = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             count += 1
#         if count >= maxcount:
#             maxcount = count
#             maxn = j
# print(maxn)


# # Даны натуральные числа n, m. Получить все числа меньше m взаимно простые с n.
# n = int(input())
# m = int(input())
# for i in range(1, m)



