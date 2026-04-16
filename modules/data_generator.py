from random import randint;

def generate_random_array(n=10, min=1, max=100):
    return [randint(min, max) for _ in range(n)];

def generate_ascending_array(n=10, min=1, max=10):
    array = [];
    current = randint(min, max);

    for _ in range(n):
        current += randint(min, max);
        array.append(current);

    return array;

def generate_descending_array(n=10, min=1, max=10):
    return generate_ascending_array(n, min, max)[::-1];

def generate_flat_array(n=10):
    return [1 for _ in range(n)];

def generate_v_shape_array(n=10, min=1, max=10):
    if n % 2 == 0:
        arr = generate_ascending_array(n // 2, min, max);
        return arr[::-1] + arr;
    else:
        arr = generate_ascending_array((n + 1) // 2, min, max);
        return arr[::-1] + arr[1::];

def main():

    #print(generate_random_array(1))
    #print(generate_random_array())
    #print(generate_random_array())
    #print(generate_random_array(min=1, max=10))
    #print(generate_random_array(min=10, max=1000))

    print(generate_ascending_array());
    print(generate_descending_array());

    #print(generate_flat_array());

    print(generate_v_shape_array());
    print(generate_v_shape_array(9));

    return 0;

if __name__ == "__main__":
    main();