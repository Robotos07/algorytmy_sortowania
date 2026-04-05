import progress_bar;
from timeit import timeit;
from file import save_profile;

def profile(func='print', start=0, end=100, repeats=1, timestamps=True, filename='output', setup=False, module='__main__', save_raw_data=False, save_result_data=False, filename_raw_data='data_raw_output', filename_result_data='data_result_output'):
    message = '';
    if timestamps:
        Progress = progress_bar.Progress(end - start, [25, 50, 75]);

    for i in range(start, end):
        if timestamps and not Progress.finished:
            Progress.advance_progress();

        message += str(timeit(func + '(' + str(i) + ',' + str(save_raw_data) + ',' + str(save_result_data) + ',"' + filename_raw_data + '","' + filename_result_data +'")', setup=('from ' + module + ' import ' + func) if setup else '', number=repeats) / repeats) + '\n';
    
    save_profile(message, filename);
    return 0;

def main():    
    Progress = progress_bar.Progress(tasks=1, timestamps=[0, 100], summary=True);
    profile(func='test_insertion_sort_random', module='tests', start=2000, end=2200, setup=True, save_raw_data=True, save_result_data=True);
    Progress.advance_progress();

    return 0;

if __name__ == "__main__":
    main();