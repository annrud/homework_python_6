# Задайте два числа. Напишите программу,
# которая найдёт НОД (наибольший общий делитель)
# и НОК (наибольший общее кратное) этих двух чисел.

a, b = [int(i) for i in input('Введите 2 числа через пробел: ').split()]


def quick_euclidean_algorithm(x, y, cnt=0):
    while y != 0:
        cnt += 1
        x, y = y, x % y
    return x


print(f'Наибольший общий делитель: {quick_euclidean_algorithm(a, b)}')
print(f'Наименьшее общее кратное: {a*b/quick_euclidean_algorithm(a, b)}')
