import random


def bubble(arr):

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    print("List after sorting: ")
    print(arr)
    print(arr == sorted(arr))


ls = [random.randint(-15, 15) for i in range(50)]
bubble(ls)
