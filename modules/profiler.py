import progress_bar;
from timeit import timeit;
from file import save_profile, save_profile_point;

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

#IS RANDOM
def main():    
    Progress = progress_bar.Progress(tasks=1, timestamps=[0, 100], summary=True);
    #profile(func='test_insertion_sort_random', module='tests', start=1000, end=1001, setup=True, step=1);
    profile_multiple(func='test_insertion_sort_random', module='tests', n_points=[1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000], repeats=10, setup=True);
    
    Progress.advance_progress();

    return 0;

#IS D
def main():    
    Progress = progress_bar.Progress(tasks=1, timestamps=[0, 100], summary=True);
    profile_multiple(func='test_insertion_sort_descending', module='tests', n_points=[1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000], repeats=10, setup=True);
    
    Progress.advance_progress();

    return 0;

#IS A
def main():    
    Progress = progress_bar.Progress(tasks=1, timestamps=[0, 100], summary=True);
    profile_multiple(func='test_insertion_sort_ascending', module='tests', n_points=[1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000], repeats=10, setup=True);
    
    Progress.advance_progress();

    return 0;

#IS F
def main():    
    Progress = progress_bar.Progress(tasks=1, timestamps=[0, 100], summary=True);
    profile_multiple(func='test_insertion_sort_flat', module='tests', n_points=[1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000], repeats=10, setup=True);
    
    Progress.advance_progress();

    return 0;

#IS V
def main():    
    Progress = progress_bar.Progress(tasks=1, timestamps=[0, 100], summary=True);
    profile_multiple(func='test_insertion_sort_v_shape', module='tests', n_points=[1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000], repeats=10, setup=True);
    
    Progress.advance_progress();

    return 0;

#SS RANDOM
def main():    
    Progress = progress_bar.Progress(tasks=1, timestamps=[0, 100], summary=True);
    profile_multiple(func='test_selection_sort_random', module='tests', n_points=[1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000], repeats=10, setup=True);
    
    Progress.advance_progress();

    return 0;

#SS D
def main():    
    Progress = progress_bar.Progress(tasks=1, timestamps=[0, 100], summary=True);
    profile_multiple(func='test_selection_sort_descending', module='tests', n_points=[1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000], repeats=10, setup=True);
    
    Progress.advance_progress();

    return 0;

#SS A
def main():    
    Progress = progress_bar.Progress(tasks=1, timestamps=[0, 100], summary=True);
    profile_multiple(func='test_selection_sort_ascending', module='tests', n_points=[1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000], repeats=10, setup=True);
    
    Progress.advance_progress();

    return 0;

#SS F
def main():    
    Progress = progress_bar.Progress(tasks=1, timestamps=[0, 100], summary=True);
    profile_multiple(func='test_selection_sort_flat', module='tests', n_points=[1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000], repeats=10, setup=True);
    
    Progress.advance_progress();

    return 0;

#SS V
def main():    
    Progress = progress_bar.Progress(tasks=1, timestamps=[0, 100], summary=True);
    profile_multiple(func='test_selection_sort_v_shape', module='tests', n_points=[1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000], repeats=10, setup=True);
    
    Progress.advance_progress();

    return 0;

#HS RANDOM
def main():    
    Progress = progress_bar.Progress(tasks=1, timestamps=[0, 100], summary=True);
    profile_multiple(func='test_heap_sort_random', module='tests', n_points=[1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000], repeats=10, setup=True);
    
    Progress.advance_progress();

    return 0;

#HS D
def main():    
    Progress = progress_bar.Progress(tasks=1, timestamps=[0, 100], summary=True);
    profile_multiple(func='test_heap_sort_descending', module='tests', n_points=[1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000], repeats=10, setup=True);
    
    Progress.advance_progress();

    return 0;

#HS A
def main():    
    Progress = progress_bar.Progress(tasks=1, timestamps=[0, 100], summary=True);
    profile_multiple(func='test_heap_sort_ascending', module='tests', n_points=[1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000], repeats=10, setup=True);
    
    Progress.advance_progress();

    return 0;

#HS F
def main():    
    Progress = progress_bar.Progress(tasks=1, timestamps=[0, 100], summary=True);
    profile_multiple(func='test_heap_sort_flat', module='tests', n_points=[1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000], repeats=10, setup=True);
    
    Progress.advance_progress();

    return 0;

#HS V
def main():    
    Progress = progress_bar.Progress(tasks=1, timestamps=[0, 100], summary=True);
    profile_multiple(func='test_heap_sort_v_shape', module='tests', n_points=[1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000], repeats=10, setup=True);
    
    Progress.advance_progress();

    return 0;

#MS RANDOM
def main():    
    Progress = progress_bar.Progress(tasks=1, timestamps=[0, 100], summary=True);
    profile_multiple(func='test_merge_sort_random', module='tests', n_points=[1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000], repeats=10, setup=True);
    
    Progress.advance_progress();

    return 0;

#MS D
def main():    
    Progress = progress_bar.Progress(tasks=1, timestamps=[0, 100], summary=True);
    profile_multiple(func='test_merge_sort_descending', module='tests', n_points=[1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000], repeats=10, setup=True);
    
    Progress.advance_progress();

    return 0;

#MS A
def main():    
    Progress = progress_bar.Progress(tasks=1, timestamps=[0, 100], summary=True);
    profile_multiple(func='test_merge_sort_ascending', module='tests', n_points=[1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000], repeats=10, setup=True);
    
    Progress.advance_progress();

    return 0;

#MS F
def main():    
    Progress = progress_bar.Progress(tasks=1, timestamps=[0, 100], summary=True);
    profile_multiple(func='test_merge_sort_flat', module='tests', n_points=[1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000], repeats=10, setup=True);
    
    Progress.advance_progress();

    return 0;

#MS V
def main():    
    Progress = progress_bar.Progress(tasks=1, timestamps=[0, 100], summary=True);
    profile_multiple(func='test_merge_sort_v_shape', module='tests', n_points=[1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000], repeats=10, setup=True);
    
    Progress.advance_progress();

    return 0;

#QS R
def main():    
    Progress = progress_bar.Progress(tasks=1, timestamps=[0, 100], summary=True);
    profile_multiple(func='test_quick_sort_random', module='tests', n_points=[1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000], repeats=10, setup=True);
    
    Progress.advance_progress();

    return 0;

#QS D
def main():    
    Progress = progress_bar.Progress(tasks=1, timestamps=[0, 100], summary=True);
    profile_multiple(func='test_quick_sort_descending', module='tests', n_points=[1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000], repeats=10, setup=True);
    
    Progress.advance_progress();

    return 0;


#QS A
def main():    
    Progress = progress_bar.Progress(tasks=1, timestamps=[0, 100], summary=True);
    profile_multiple(func='test_quick_sort_ascending', module='tests', n_points=[1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000], repeats=10, setup=True);
    
    Progress.advance_progress();

    return 0;


#QS F
def main():    
    Progress = progress_bar.Progress(tasks=1, timestamps=[0, 100], summary=True);
    profile_multiple(func='test_quick_sort_flat', module='tests', n_points=[1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000], repeats=10, setup=True);
    
    Progress.advance_progress();

    return 0;


#QS V
def main():    
    Progress = progress_bar.Progress(tasks=1, timestamps=[0, 100], summary=True);
    profile_multiple(func='test_quick_sort_v_shape', module='tests', n_points=[1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000], repeats=10, setup=True);
    
    Progress.advance_progress();

    return 0;

if __name__ == "__main__":
    main();