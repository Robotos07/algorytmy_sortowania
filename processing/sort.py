import random;

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

def main():
    print(heap_sort([6, 3, 1, 6, 8, 7]))
    print(heap_sort([x*x for x in range(10)]))
    rand_arr = [random.randint(1, 100) for x in range(200)]
    print(rand_arr);
    print(heap_sort(rand_arr))

    return 0;

if __name__ == "__main__":
    main();