import sort
import progress_bar
from random import randint
from timeit import timeit

def test(x):
    sort.insertion_sort([randint(1, 100) for x in range(x)]);
    return 0;

def profile(start=0, end=100, repeats=1, timestamps=True):
    message = '';
    if timestamps:
        Progress = progress_bar.Progress(end - start, [25, 50, 75])

    for i in range(start, end):
        if timestamps and not Progress.finished:
            Progress.advance_progress();

        message += str(timeit('test(' + str(i) + ')', setup='from __main__ import test', number=repeats) / repeats) + '\n';
    
    save(message);
    return 0;

def main():    
    Progress = progress_bar.Progress(tasks=1, timestamps=[0, 100], summary=True)
    profile(start=2000, end=2200);
    Progress.advance_progress();

    return 0;

def save(message, filename='output.txt'):
    with open(filename, 'w') as file:
        file.write(message);
    return 0;

if __name__ == "__main__":
    main();