import progress_bar;
from timeit import timeit;

def profile(func='print', start=0, end=100, repeats=1, timestamps=True, filename='output', setup=False, module='__main__'):
    message = '';
    if timestamps:
        Progress = progress_bar.Progress(end - start, [25, 50, 75]);

    for i in range(start, end):
        if timestamps and not Progress.finished:
            Progress.advance_progress();

        message += str(timeit(func + '(' + str(i) + ')', setup=('from ' + module + ' import ' + func) if setup else '', number=repeats) / repeats) + '\n';
    
    save(message, filename);
    return 0;

def main():    
    Progress = progress_bar.Progress(tasks=1, timestamps=[0, 100], summary=True);
    profile(func='test_insertion_sort_random', module='tests', start=2000, end=2200, setup=True);
    Progress.advance_progress();

    return 0;

def save(message, filename='output'):
    with open(filename + '.txt', 'w') as file:
        file.write(message);
    return 0;

if __name__ == "__main__":
    main();