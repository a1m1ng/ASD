def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # Начальное расстояние между элементами (можно использовать другие способы выбора интервала)

    while gap > 0:
        for i in range(gap, n):
            current_element = arr[i]
            j = i

            # Сортируем элементы на расстоянии gap друг от друга
            while j >= gap and arr[j - gap] > current_element:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = current_element

        gap //= 2  # Уменьшаем интервал

my_list = [24, 543, 5, 21, 74]
shell_sort(my_list)
print(my_list)