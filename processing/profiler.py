import sort
import progress_bar
from random import randint
from timeit import timeit

def test(x):
    sort.insertion_sort([randint(1, 100) for x in range(x)]);
    return 0;

def profile(func='print', start=0, end=100, repeats=1, timestamps=True, filename='output', setup=False, module='__main__'):
    message = '';
    if timestamps:
        Progress = progress_bar.Progress(end - start, [25, 50, 75])

    for i in range(start, end):
        if timestamps and not Progress.finished:
            Progress.advance_progress();

        message += str(timeit(func + '(' + str(i) + ')', setup=('from ' + module + ' import ' + func) if setup else '', number=repeats) / repeats) + '\n';
    
    save(message, filename);
    return 0;

def main():    
    Progress = progress_bar.Progress(tasks=1, timestamps=[0, 100], summary=True)
    profile(func='test', start=0, end=2200, setup=True);
    Progress.advance_progress();

    return 0;

def save(message, filename='output'):
    with open(filename + '.txt', 'w') as file:
        file.write(message);
    return 0;

if __name__ == "__main__":
    main();