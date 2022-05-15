def insertionSort(arr):
    for i in range(len(arr)-1):
        key = arr[i+1]
        j = i
        while j >= 0 and key < arr[j] :
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


array = [22,27,16,2,18,6]
insertionSort(array)
print(array)
