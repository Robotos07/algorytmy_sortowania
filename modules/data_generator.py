from random import randint;

def generate_random_array(n=10, min=1, max=100):
    return [randint(min, max) for _ in range(n)];

def main():

    print(generate_random_array(1))
    print(generate_random_array())
    print(generate_random_array())
    print(generate_random_array(min=1, max=10))
    print(generate_random_array(min=10, max=1000))

    return 0;

if __name__ == "__main__":
    main();