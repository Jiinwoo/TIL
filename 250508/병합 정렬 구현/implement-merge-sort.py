n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def merge_sort(arr, start, end):
    if start < end:
        mid = start + (end - start) // 2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid + 1, end)
        merge(arr, start, mid, end)

def merge(arr, start, mid, end):
    i, j = start, mid + 1
    merged = []
    while i <= mid and j <= end:
        if arr[i] <= arr[j]:
            merged.append(arr[i])
            i += 1
        else:
            merged.append(arr[j])
            j += 1
    while i <= mid:
        merged.append(arr[i])
        i += 1
    while j <= end:
        merged.append(arr[j])
        j += 1

    for i in range(len(merged)):
        arr[start + i] = merged[i]
    return arr

merge_sort(arr, 0, n-1)
print(*arr) 