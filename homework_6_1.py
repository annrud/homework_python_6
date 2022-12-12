# Напишите программу вычисления арифметического выражения
# заданного строкой. Используйте операции +,-,/,*.
# приоритет операций стандартный.

with open('arithmetic_expression.txt', 'r') as f:
    exp = f.readline().split()

exp = list(map(lambda i: float(i) if i.isdigit() else i, exp))


def add_sign(args):
    for i in range(len(args)-1):
        if args[i] == '-' and args[i+1] != '(':
            args[i + 1] *= -1
            if args[i-1] == '(' or i == 0:
                args.pop(i)
            else:
                args[i] = '+'


def reduce_args(args, index, sign):
    if sign == '*':
        args[index - 1] *= args[index + 1]
    elif sign == '/':
        args[index - 1] /= args[index + 1]
    elif sign == '+':
        args[index - 1] += args[index + 1]
    elif sign == '-':
        args[index - 1] -= args[index + 1]
    args.pop(index + 1)
    args.pop(index)


def priority(args, sign1, sign2):
    while sign1 in args or sign2 in args:
        sign1_index = args.index(sign1) if sign1 in args else 100
        sign2_index = args.index(sign2) if sign2 in args else 100
        if sign1_index < sign2_index:
            reduce_args(args, sign1_index, sign1)
        else:
            reduce_args(args, sign2_index, sign2)
    return args


def solution(args):
    while len(args) > 2:
        priority(args, '*', '/')
        priority(args, '+', '-')
    return args[0]


def find_parentheses(args):
    add_sign(args)
    while '(' in args:
        args_slice = args[args.index('(') + 1: args.index(')')]
        del args[args.index('(') + 1: args.index(')')+1]
        args[args.index('(')] = solution(args_slice)
        add_sign(args)
    return args


print(f'Ответ: {solution(find_parentheses(exp))}')
