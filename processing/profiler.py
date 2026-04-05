import sort
from random import randint
from timeit import timeit

def test(x):
    sort.insertion_sort([randint(1, 100) for x in range(x)]);
    return 0;

def profile(start=0, end=100, repeats=1):
    message = '';
    
    for i in range(start, end):
        message += str(timeit('test(' + str(i) + ')', setup='from __main__ import test', number=repeats) / repeats) + '\n';
    
    save(message);
    return 0;

def main():    
    # timeit('test()', setup='from __main__ import test', number=1)
    print('start')
    profile(start=2000, end=2200);
    print('end');
    return 0;

def save(message, filename='output.txt'):
    with open(filename, 'w') as file:
        file.write(message);
    return 0;

if __name__ == "__main__":
    main();