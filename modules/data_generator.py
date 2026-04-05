from random import randint;

def generate_random_array(n=10, min=1, max=100):
    return [randint(min, max) for _ in range(n)];

def generate_ascending_array(n=10, min=1, max=10):
    if n == 1: 
        return [randint(min, max)];

    arr = generate_ascending_array(n-1, min, max);
    return arr + [arr[len(arr) - 1] + randint(min, max)];

def generate_descending_array(n=10, min=1, max=10):
    return generate_ascending_array(n, min, max)[::-1];

def generate_flat_array(n=10):
    return [1 for _ in range(n)];

def main():

    #print(generate_random_array(1))
    #print(generate_random_array())
    #print(generate_random_array())
    #print(generate_random_array(min=1, max=10))
    #print(generate_random_array(min=10, max=1000))

    #print(generate_ascending_array());
    #print(generate_descending_array());

    print(generate_flat_array());

    return 0;

if __name__ == "__main__":
    main();