from random import randint;

def insertion_sort(unsorted_array):
    for j in range(1, len(unsorted_array)):
        key = unsorted_array[j];
        i = j - 1;
        while (i >= 0) and (unsorted_array[i] > key):
            unsorted_array[i + 1] = unsorted_array[i];
            i = i - 1
        unsorted_array[i + 1] = key;
    return unsorted_array;

def selection_sort(unsorted_array):
    for idx in range(len(unsorted_array) - 1):
        min_idx = idx

        for j in range(idx + 1, len(unsorted_array)):
            if unsorted_array[j] < unsorted_array[min_idx]:
                min_idx = j

        unsorted_array[idx], unsorted_array[min_idx] = unsorted_array[min_idx], unsorted_array[idx]
    return unsorted_array;

def heapify(unsorted_array, n, i):
    largest = i    
    l = 2 * i + 1    
    r = 2 * i + 2  

    if l < n and unsorted_array[l] > unsorted_array[largest]:
        largest = l

    if r < n and unsorted_array[r] > unsorted_array[largest]:
        largest = r

    if largest != i:
        unsorted_array[i], unsorted_array[largest] = unsorted_array[largest], unsorted_array[i]
        heapify(unsorted_array, n, largest)

def heap_sort(unsorted_array):
    n = len(unsorted_array)

    for i in range(n // 2 - 1, -1, -1): # Build Heap
        heapify(unsorted_array, n, i)

    for i in range(n - 1, 0, -1):
        unsorted_array[i], unsorted_array[0] = unsorted_array[0], unsorted_array[i]  # Swap max to end
        heapify(unsorted_array, i, 0)
    return unsorted_array;

def merge(unsorted_array, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = unsorted_array[l + i]
    for j in range(n2):
        R[j] = unsorted_array[m + 1 + j]

    i = j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            unsorted_array[k] = L[i]
            i += 1
        else:
            unsorted_array[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        unsorted_array[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        unsorted_array[k] = R[j]
        j += 1
        k += 1

def merge_sort(unsorted_array, l, r):
    if l < r:
        m = l + (r - l) // 2
        merge_sort(unsorted_array, l, m)
        merge_sort(unsorted_array, m + 1, r)
        merge(unsorted_array, l, m, r)

def merge_sort_main(unsorted_array):
    merge_sort(unsorted_array, 0, len(unsorted_array) - 1)
    return unsorted_array;

def create_pivot_idx(mode, end):
    if mode == 'first':
        return 0;
    if mode == 'last':
        return end;
    if mode == 'random':
        return randint(0, end)
    if mode == 'middle':
        return end // 2;


def quick_sort(arr, mode):
    if len(arr) <= 1:
        return arr;

    pivot_idx = create_pivot_idx(mode, len(arr)-1)
    pivot = arr[pivot_idx]
    left = ([x for x in arr[:pivot_idx] if x < pivot] if pivot_idx > 0 else []  ) + ([x for x in arr[pivot_idx + 1:] if x < pivot] if pivot_idx < len(arr) else [])
    right = ([x for x in arr[:pivot_idx] if x >= pivot] if pivot_idx > 0 else [])  + ([x for x in arr[pivot_idx + 1:] if x >= pivot] if pivot_idx < len(arr) else [])

    return quick_sort(left, mode) + [pivot] + quick_sort(right, mode)

def main():
    print(quick_sort([6, 3, 1, 6, 8, 7], 'middle'))
    print(quick_sort([x*x for x in range(10)], 'middle'))
    rand_arr = [randint(1, 100) for x in range(50)]
    print(rand_arr);
    print(quick_sort(rand_arr, 'middle'))

    return 0;

if __name__ == "__main__":
    main();