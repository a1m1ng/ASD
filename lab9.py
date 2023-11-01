# Преобразование корня i двоичного поддерева в корень кучи
def heapify(arr, n, i):
    largest = i 
    l = 2 * i + 1
    r = 2 * i + 2

  # Проверяем существует ли левый дочерний элемент больший, чем корень

    if l < n and arr[i] < arr[l]:
        largest = l

    # Проверяем существует ли правый дочерний элемент больший, чем корень

    if r < n and arr[largest] < arr[r]:
        largest = r

    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i] # Заменяем корень

        # Применяем heapify к корню.
        heapify(arr, n, largest)

# Основная функция для сортировки массива
def heapSort(arr):
    n = len(arr)

    # Построение max-heap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # Один за другим извлекаем элементы
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # свап 
        heapify(arr, i, 0)

# Управляющий код для тестирования
arr = [ 12, 11, 13, 5, 6, 7]
heapSort(arr)
print(arr)
