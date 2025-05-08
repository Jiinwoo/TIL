n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def quick_sort(arr, start, end):
    if start < end:
        pos = conquer(arr, start, end)
        quick_sort(arr, start, pos-1)
        quick_sort(arr, pos+1, end)

def conquer(arr, start, end):
    pivot = arr[end]
    i = start - 1
    j = start
    while j < end:
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1
    arr[i+1], arr[end] = arr[end], arr[i+1]
    return i + 1

quick_sort(arr, 0, n-1)
print(*arr)