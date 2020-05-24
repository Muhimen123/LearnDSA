def merge(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result

def merge_sort(ls):
    if len(ls) <= 1:
        return ls
    else:
        mid = len(ls) // 2
        left = merge_sort(ls[:mid])
        right = merge_sort(ls[mid:])

        return merge(left, right)

test = [3,1,5,3,2,5,-8,2,9,-6,12,-53,75,22,83,-123,12123]
print(merge_sort(test))
