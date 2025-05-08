n = int(input())
arr = [0] + list(map(int, input().split()))

# Please write your code here.
def heap_sort(arr, n):
    end = n // 2
    for i in range(end, 0, -1):
        heapify(arr, n, i)
    for i in range(n, 0, -1):
        arr[1], arr[i] = arr[i], arr[1]
        heapify(arr, i-1, 1)
    
def heapify(arr, n, i):
    largest = i
    l = i * 2
    r = i * 2 + 1
    if l <= n and arr[l] > arr[largest]:
        largest = l
    if r <= n  and arr[r] > arr[largest]:
        largest = r
    if arr[largest] != arr[i]:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

heap_sort(arr, n)
print(*arr[1:])