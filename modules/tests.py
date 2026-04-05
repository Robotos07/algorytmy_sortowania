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

def main():
    return 0;

if __name__ == "__main__":
    main();