def radix_sort(arr):
    # Находим длину наибольшего числа
    max_digits = max([len(str(x)) for x in arr])

    base = 10

    bins = [[] for _ in range(base)]

    for i in range(max_digits):
        for x in arr:
            # Получаем цифру, стоящую на текущем разряде в каждом числе массива
            digit = (x // base ** i) % base
            bins[digit].append(x)

        # Cобираем в исходный массив значения из промежуточного массива
        arr = [x for queue in bins for x in queue]

        bins = [[] for _ in range(base)]
    return arr

my_list = [24, 543, 5, 21, 74]
print(radix_sort(my_list))
