def quit_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]

        return quit_sort(less) + [pivot] + quit_sort(greater)

my_list = [24, 543, 5, 21, 74]
print(quit_sort(my_list))