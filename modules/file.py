def save_data(array: list, filename='data_output', overwrite=False) -> int:
    with open(filename + '.txt', 'w' if overwrite else 'a') as file:
        for idx in range(len(array)):
            file.write(str(array[idx]) + ('; ' if idx != len(array) else ''));
        file.write('\n');
    return 0;

def save_profile(message: str, filename='output', overwrite=True) -> int:
    with open(filename + '.txt', 'w' if overwrite else 'a') as file:
        message = message.replace('.', ',');
        file.write(message);
    return 0;

def save_profile_point(time: float, filename='output', overwrite=False) -> int:
    with open(filename + '.txt', 'w' if overwrite else 'a') as file:
        file.write(str(time));
    return 0;

def load_data(filename='data_output') -> list:
    data = [];
    with open(filename + '.txt', 'r') as file:
        raw = file.readlines();
        raw_temp = [];
        for line in raw:
            raw_temp += line.split(';');
        raw = [element.strip() for element in raw_temp];
    
        data = [int(element) for element in raw if element != '' and element != '\n'];
        
    return data;

def write(filename, n, weights, values, capacity):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"{n}\n")
        f.write(" ".join(map(str, weights)) + "\n")
        f.write(" ".join(map(str, values)) + "\n")
        f.write(str(capacity))

def read(filename):
    with open(filename, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    n = int(lines[0])
    weights = list(map(int, lines[1].split()))
    values = list(map(int, lines[2].split()))
    capacity = int(lines[3])

    return n, weights, values, capacity

def write_list(filename, data):
    with open(filename, "w", encoding="utf-8") as f:
        for x in data:
            f.write(f"{x}\n")