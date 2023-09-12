staples = {')' : '(', '}' : '{', ']': '['}

s = input('Введите строку: ')

# 1. Количество закрытых скобок больше
# 2. Количество открытых скобок больше
# 3. Закрывающая скобка не соответсвует открывающей

def check_staples(string_staples):
    stack = []

    for i in s:
        if i in staples.values():
            stack.append(i)
        else:
            if not stack or staples[i] != stack.pop():
                return False
    if stack:
        return False
    else:
        return True

res = check_staples(s)
if res:
    print('Строка существует')
else:
    print('Строка не существует')