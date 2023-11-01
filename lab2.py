# Первая лабораторная
def check_staples(string_staples):
    staples = {')' : '(', '}' : '{', ']': '['}
    stack = []

    for i in string_staples:
        if i in staples.values():
            stack.append(i)
        elif i in staples.keys():
            if not stack or staples[i] != stack.pop():
                return False
    if stack:
        return False
    else:
        return True


# Приведение выражение к виду массива операторов и операндов
def to_tokens(exp):
    if not check_staples(exp):
        raise Exception('Неверное скобочное выражение')

    tokens = []
    num = ''
    for i in range(len(exp)):
        if exp[i].isdigit():
            num += exp[i]
            continue
        elif exp[i] == '-' and (i == 0 or exp[i-1] == '('):
            num += exp[i]
            continue
        elif num:
            tokens.append(int(num))
            num = ''
        tokens.append(exp[i])
    if num:
        tokens.append(int(num))
    return tokens


PRIORITY = {'+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '^': 3}

# Приведение выражения к обратной польской записи
def poland(s):
    tokens = to_tokens(s)
    res = []
    stack = []
    while tokens:
        el = tokens.pop(0)
        if isinstance(el, int):
            res.append(el)
        
        elif el in '+-*/^':
            while stack and PRIORITY.get(stack[-1], 0) >= PRIORITY.get(el, 1):
                res.append(stack.pop())
            stack.append(el)

        elif el == '(':
            stack.append('(')

        elif el == ')':
            while stack[-1] != '(':
                res.append(stack.pop())
            stack.pop()

    while stack:
        res += stack.pop()

    return res

OPERATORS = {'+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
            '^': lambda x, y: x**y}

def poland_calculate(exp):
    poland_exp = poland(exp)
    stack = []

    while poland_exp:
        token = poland_exp.pop(0)
        if isinstance(token, int):
            stack.append(token)
        else:
            y = stack.pop()
            x = stack.pop()

            if token == '/' and y == 0:
                raise Exception('Вы попытались разделить на 0')

            stack.append(OPERATORS[token](x, y))
    return stack[0]

s = '20+((21-7)*9)-10'

print(poland_calculate('5 + ((1 + 2) * 4) - 3'))    #14
print(poland_calculate('3 + 4 * 2 / (1 - 5)^2'))    #3.5
print(poland_calculate(s))  # 136

print(poland_calculate('5*(-3 * 2) + 2'))

print(poland_calculate('2+7*(3/9)-5='))

print(poland_calculate('()1+2'))
