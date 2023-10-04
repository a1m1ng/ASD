def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        
        # Находим индекс минимального элемента в оставшейся части массива
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Обмениваем текущий элемент с минимальным элементом
        arr[i], arr[min_index] = arr[min_index], arr[i]

my_list = [24, 543, 5, 21, 74]
selection_sort(my_list)
print(my_list)