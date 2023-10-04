def comb_sort(arr):
    gap = len(arr)
    factor = 1.2473309  # Множитель, определяющий, на сколько уменьшать интервал

    swapped = True  # Была ли перестановка
    while gap > 1 or swapped:
        gap = int(gap / factor) # Вычисляем новый интервал
        gap = max(1, gap)  # Минимальное значение интервала равно 1

        swapped = False
        for i in range(len(arr) - gap):
            j = i + gap
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                swapped = True

my_list = [24, 543, 5, 21, 74]
comb_sort(my_list)
print(my_list)