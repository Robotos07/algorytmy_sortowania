import sort;
import data_generator;

def test_insertion_sort_random(x):
    raw = data_generator.generate_random_array(x);
    sort.insertion_sort(raw[:]);

    return 0;

def test_insertion_sort_ascending(x):
    raw = data_generator.generate_ascending_array(x);
    sort.insertion_sort(raw[:]);

    return 0;

def main():
    return 0;

if __name__ == "__main__":
    main();