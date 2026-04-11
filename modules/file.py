def save_data(array, filename='data_output', overwrite=False):
    with open(filename + '.txt', 'w' if overwrite else 'a') as file:
        for idx in range(len(array)):
            file.write(str(array[idx]) + ('; ' if idx != len(array) else ''));
        file.write('\n');
    return 0;

def save_profile(message, filename='output', overwrite=True):
    with open(filename + '.txt', 'w' if overwrite else 'a') as file:
        file.write(message);
    return 0;

def save_profile_point(time, filename='output', overwrite=False):
    with open(filename + '.txt', 'w' if overwrite else 'a') as file:
        file.write(str(time));
    return 0;