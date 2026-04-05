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

def main():
    print(selection_sort([6, 3, 1, 6, 8, 7]))
    print(selection_sort([x*x for x in range(10)]))
    rand_arr = [random.randint(1, 100) for x in range(200)]
    print(rand_arr);
    print(selection_sort(rand_arr))

    return 0;

if __name__ == "__main__":
    main();