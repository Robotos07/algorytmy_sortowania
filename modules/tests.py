import sort;
import data_generator;
import file;

def test_insertion_sort_random(x, save_raw=False, save_result=False, filename_raw='data_raw_output', filename_result='data_result_output'):
    raw = data_generator.generate_random_array(x);
    result = sort.insertion_sort(raw[:]);

    if save_raw:
        file.save_data(raw, filename_raw);
    if save_result:
        file.save_data(result, filename_result);

    return 0;

def test_insertion_sort_ascending(x, save_raw=False, save_result=False, filename_raw='data_raw_output', filename_result='data_result_output'):
    raw = data_generator.generate_ascending_array(x);
    result = sort.insertion_sort(raw[:]);

    if save_raw:
        file.save_data(raw, filename_raw);
    if save_result:
        file.save_data(result, filename_result);

    return 0;

def test_insertion_sort_descending(x, save_raw=False, save_result=False, filename_raw='data_raw_output', filename_result='data_result_output'):
    raw = data_generator.generate_descending_array(x);
    result = sort.insertion_sort(raw[:]);

    if save_raw:
        file.save_data(raw, filename_raw);
    if save_result:
        file.save_data(result, filename_result);

    return 0;

def test_insertion_sort_flat(x, save_raw=False, save_result=False, filename_raw='data_raw_output', filename_result='data_result_output'):
    raw = data_generator.generate_flat_array(x);
    result = sort.insertion_sort(raw[:]);

    if save_raw:
        file.save_data(raw, filename_raw);
    if save_result:
        file.save_data(result, filename_result);

    return 0;

def test_insertion_sort_v_shape(x, save_raw=False, save_result=False, filename_raw='data_raw_output', filename_result='data_result_output'):
    raw = data_generator.generate_v_shape_array(x);
    result = sort.insertion_sort(raw[:]);

    if save_raw:
        file.save_data(raw, filename_raw);
    if save_result:
        file.save_data(result, filename_result);

    return 0;

def test_selection_sort_random(x, save_raw=False, save_result=False, filename_raw='data_raw_output', filename_result='data_result_output'):
    raw = data_generator.generate_random_array(x);
    result = sort.selection_sort(raw[:]);

    if save_raw:
        file.save_data(raw, filename_raw);
    if save_result:
        file.save_data(result, filename_result);

    return 0;

def test_selection_sort_ascending(x, save_raw=False, save_result=False, filename_raw='data_raw_output', filename_result='data_result_output'):
    raw = data_generator.generate_ascending_array(x);
    result = sort.selection_sort(raw[:]);

    if save_raw:
        file.save_data(raw, filename_raw);
    if save_result:
        file.save_data(result, filename_result);

    return 0;

def test_selection_sort_descending(x, save_raw=False, save_result=False, filename_raw='data_raw_output', filename_result='data_result_output'):
    raw = data_generator.generate_descending_array(x);
    result = sort.selection_sort(raw[:]);

    if save_raw:
        file.save_data(raw, filename_raw);
    if save_result:
        file.save_data(result, filename_result);

    return 0;

def test_selection_sort_flat(x, save_raw=False, save_result=False, filename_raw='data_raw_output', filename_result='data_result_output'):
    raw = data_generator.generate_flat_array(x);
    result = sort.selection_sort(raw[:]);

    if save_raw:
        file.save_data(raw, filename_raw);
    if save_result:
        file.save_data(result, filename_result);

    return 0;

def test_selection_sort_v_shape(x, save_raw=False, save_result=False, filename_raw='data_raw_output', filename_result='data_result_output'):
    raw = data_generator.generate_v_shape_array(x);
    result = sort.selection_sort(raw[:]);

    if save_raw:
        file.save_data(raw, filename_raw);
    if save_result:
        file.save_data(result, filename_result);

    return 0;

def test_heap_sort_random(x, save_raw=False, save_result=False, filename_raw='data_raw_output', filename_result='data_result_output'):
    raw = data_generator.generate_random_array(x);
    result = sort.heap_sort(raw[:]);

    if save_raw:
        file.save_data(raw, filename_raw);
    if save_result:
        file.save_data(result, filename_result);

    return 0;

def test_heap_sort_ascending(x, save_raw=False, save_result=False, filename_raw='data_raw_output', filename_result='data_result_output'):
    raw = data_generator.generate_ascending_array(x);
    result = sort.heap_sort(raw[:]);

    if save_raw:
        file.save_data(raw, filename_raw);
    if save_result:
        file.save_data(result, filename_result);

    return 0;

def test_heap_sort_descending(x, save_raw=False, save_result=False, filename_raw='data_raw_output', filename_result='data_result_output'):
    raw = data_generator.generate_descending_array(x);
    result = sort.heap_sort(raw[:]);

    if save_raw:
        file.save_data(raw, filename_raw);
    if save_result:
        file.save_data(result, filename_result);

    return 0;

def test_heap_sort_flat(x, save_raw=False, save_result=False, filename_raw='data_raw_output', filename_result='data_result_output'):
    raw = data_generator.generate_flat_array(x);
    result = sort.heap_sort(raw[:]);

    if save_raw:
        file.save_data(raw, filename_raw);
    if save_result:
        file.save_data(result, filename_result);

    return 0;

def test_heap_sort_v_shape(x, save_raw=False, save_result=False, filename_raw='data_raw_output', filename_result='data_result_output'):
    raw = data_generator.generate_v_shape_array(x);
    result = sort.heap_sort(raw[:]);

    if save_raw:
        file.save_data(raw, filename_raw);
    if save_result:
        file.save_data(result, filename_result);

    return 0;

def test_merge_sort_random(x, save_raw=False, save_result=False, filename_raw='data_raw_output', filename_result='data_result_output'):
    raw = data_generator.generate_random_array(x);
    result = sort.merge_sort(raw[:]);

    if save_raw:
        file.save_data(raw, filename_raw);
    if save_result:
        file.save_data(result, filename_result);

    return 0;

def test_merge_sort_ascending(x, save_raw=False, save_result=False, filename_raw='data_raw_output', filename_result='data_result_output'):
    raw = data_generator.generate_ascending_array(x);
    result = sort.merge_sort(raw[:]);

    if save_raw:
        file.save_data(raw, filename_raw);
    if save_result:
        file.save_data(result, filename_result);

    return 0;

def test_merge_sort_descending(x, save_raw=False, save_result=False, filename_raw='data_raw_output', filename_result='data_result_output'):
    raw = data_generator.generate_descending_array(x);
    result = sort.merge_sort(raw[:]);

    if save_raw:
        file.save_data(raw, filename_raw);
    if save_result:
        file.save_data(result, filename_result);

    return 0;

def test_merge_sort_flat(x, save_raw=False, save_result=False, filename_raw='data_raw_output', filename_result='data_result_output'):
    raw = data_generator.generate_flat_array(x);
    result = sort.merge_sort(raw[:]);

    if save_raw:
        file.save_data(raw, filename_raw);
    if save_result:
        file.save_data(result, filename_result);

    return 0;

def test_merge_sort_v_shape(x, save_raw=False, save_result=False, filename_raw='data_raw_output', filename_result='data_result_output'):
    raw = data_generator.generate_v_shape_array(x);
    result = sort.merge_sort(raw[:]);

    if save_raw:
        file.save_data(raw, filename_raw);
    if save_result:
        file.save_data(result, filename_result);

    return 0;

def test_quick_sort_random(x: int, save_result=False, filename_result='data_result_quick_sort_random_'):
    raw = file.load_data(filename='data_for_quick_sort_' + str(x))
    result = sort.quick_sort(raw[:], "random");

    if save_result:
        file.save_data(result, filename_result + str(x));

    return 0;

def test_quick_sort_middle(x: int, save_result=False, filename_result='data_result_quick_sort_middle_'):
    raw = file.load_data(filename='data_for_quick_sort_' + str(x))
    result = sort.quick_sort(raw[:], "middle");

    if save_result:
        file.save_data(result, filename_result + str(x));

    return 0;

def test_quick_sort_last(x: int, save_result=False, filename_result='data_result_quick_sort_last_'):
    raw = file.load_data(filename='data_for_quick_sort_' + str(x))
    result = sort.quick_sort(raw[:], "last");

    if save_result:
        file.save_data(result, filename_result + str(x));

    return 0;

def setup_quick_sort_data(x: int):
    raw = data_generator.generate_v_shape_array(x);

    file.save_data(raw, filename='data_for_quick_sort_' + str(x), overwrite=True);

    return 0;