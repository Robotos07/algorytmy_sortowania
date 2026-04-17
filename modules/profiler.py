import progress_bar;
from timeit import timeit;
from file import save_profile;
from dictionaries import tests_dictionary;

def profile(func='print', start=0, end=100, repeats=1, timestamps=True, filename='output', setup=False, module='__main__', save_raw_data=False, save_result_data=False, filename_raw_data='data_raw_output', filename_result_data='data_result_output', step=10):
    message = '';
    if timestamps:
        Progress = progress_bar.Progress(end - start, [25, 50, 75]);

    for i in range(start, (end + 1)):
        if timestamps and not Progress.finished:
            Progress.advance_progress();

        time = timeit(func + '(' + str(i) + ',' + str(save_raw_data) + ',' + str(save_result_data) + ',"' + filename_raw_data + '","' + filename_result_data +'")', setup=('from ' + module + ' import ' + func) if setup else '', number=repeats) / repeats;

        if i % step == 0:       
            message += str(time) + '\n';
    
    save_profile(message, filename);
    return 0;

def profile_point(func='print', n=100, repeats=1, setup=False, module='__main__'):
    return timeit(func + '(' + str(n) + ')', setup=('from ' + module + ' import ' + func) if setup else '', number=repeats) / repeats;

def profile_multiple(n_points=[100], func='print', repeats=1, setup=False, module='__main__', filename='output'):
    message = '';
    for n in n_points:
        message += str(profile_point(n=n, func=func, repeats=repeats, setup=setup, module=module)) + '\n';

    save_profile(message, filename)
    return 0;

def main():    
    Progress = progress_bar.Progress(tasks=5, timestamps=[0, 25, 50, 75, 100], summary=True);
    tests = [];
    for func_name, n_points in tests_dictionary().items():
        if "quick_sort" in func_name:
            tests += [{ 'func': func_name, 'n_points': n_points }];

    Progress.advance_progress();

    for test in tests:
        profile_multiple(func=test['func'], module='tests', n_points=test['n_points'], repeats=10, setup=True, filename=test['func'] + '_output');
        Progress.advance_progress();
    
    Progress.advance_progress();

    return 0;

if __name__ == "__main__":
    main();
    #profile_multiple(func='setup_quick_sort_data', module='tests', n_points=[980], repeats=1, setup=True)
    #profile_multiple(func='test_quick_sort_middle', module='tests', n_points=[980], repeats=1, setup=True)