def merge_sort(arr):
    if len(arr) == 1 or len(arr) == 0:
        return arr

    # Рекурсивно сортируем половины массива
    L = merge_sort(arr[:len(arr) // 2])
    R = merge_sort(arr[len(arr) // 2:])

    n = m = k = 0
    # Сливаем половины отсортированные половины в исходный массив
    while n < len(L) and m < len(R):
        if L[n] <= R[m]:
            arr[k] = L[n]
            n += 1
        else:
            arr[k] = R[m]
            m += 1
        k += 1

    while n < len(L):
        arr[k] = L[n]
        n += 1
        k += 1

    while m < len(R):
        arr[k] = R[m]
        m += 1
        k += 1
    return arr



my_list = [24, 543, 5, 21, 74]
print(merge_sort(my_list))