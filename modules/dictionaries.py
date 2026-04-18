def tests_dictionary() -> dict:
    # [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000];
    quicksort_data_points = [100, 200, 300, 400, 500, 600, 700, 800, 900];
    merge_sort_data = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000, 150000];
    heap_sort_data = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000, 150000];
    selection_sort_data = [5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000];
    insertion_sort_data = [5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000];

    return {
    'test_insertion_sort_random': insertion_sort_data,
    'test_insertion_sort_descending': insertion_sort_data,
    'test_insertion_sort_ascending': insertion_sort_data,
    'test_insertion_sort_flat': insertion_sort_data,
    'test_insertion_sort_v_shape': insertion_sort_data,

    'test_selection_sort_random': selection_sort_data,
    'test_selection_sort_descending': selection_sort_data,
    'test_selection_sort_ascending': selection_sort_data,
    'test_selection_sort_flat': selection_sort_data,
    'test_selection_sort_v_shape': selection_sort_data,

    'test_heap_sort_random': heap_sort_data,
    'test_heap_sort_descending': heap_sort_data,
    'test_heap_sort_ascending': heap_sort_data,
    'test_heap_sort_flat': heap_sort_data,
    'test_heap_sort_v_shape': heap_sort_data,

    'test_merge_sort_random': merge_sort_data,
    'test_merge_sort_descending': merge_sort_data,
    'test_merge_sort_ascending': merge_sort_data,
    'test_merge_sort_flat': merge_sort_data,
    'test_merge_sort_v_shape': merge_sort_data,
    
    'setup_quick_sort_data': quicksort_data_points,
    'test_quick_sort_random': quicksort_data_points,
    'test_quick_sort_last': quicksort_data_points,
    'test_quick_sort_middle': quicksort_data_points,
}