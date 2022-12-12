print('Программа выведет список неповторяющихся '
      'элементов исходной последовательности')
while True:
    numbers = input('Введите целые числа через пробел: ').split()
    for number in numbers:
        if not number.isdigit():
            print('Неверно введены числа!')
            break
        continue
    else:
        break


lst = list(map(int, numbers))

repeat_list = [x for i, x in enumerate(lst) if i != lst.index(x)]

print(list(set(lst) - set(repeat_list)))
