def mergeSort(arr):
    if len(arr) >= 2:
        mid = len(arr)//2
        Left = arr[:mid]
        Right = arr[mid:]
        mergeSort(Left)
        mergeSort(Right)
        
        i_L = i_R = i_arr = 0
        while len(Left) > i_L and len(Right) > i_R:
            if Left[i_L] < Right[i_R]:
                arr[i_arr] = Left[i_L]
                i_L += 1
            else:
                arr[i_arr] = Right[i_R]
                i_R += 1
            i_arr += 1

        while len(Left) > i_L:
            arr[i_arr] = Left[i_L]
            i_L += 1
            i_arr += 1

        while len(Right) > i_R:
            arr[i_arr] = Right[i_R]
            i_R += 1
            i_arr += 1


array = [16,21,11,8,12,22]
mergeSort(array)
print(array)
