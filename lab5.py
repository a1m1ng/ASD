def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_element = arr[i]
        j = i - 1

        # Сдвигаем все элементы больше текущего
        while j >= 0 and arr[j] > current_element:
            arr[j + 1] = arr[j]
            j -= 1

        # Вставляем текущий элемент на правильное место
        arr[j + 1] = current_element


my_list = [24, 543, 5, 21, 74]
insertion_sort(my_list)
print(my_list)