import data_generator;
import file;
import points;

file.save_data("", 'random_tab', True)
tab = set()

while len(tab) < points.il:
    r = data_generator.generate_random_array(points.il, 1000, 1000000)
    for x in r:
        tab.add(x)
        if len(tab) == points.il:
            break

tab = list(tab)
for element in tab:
    file.save_data([element], 'random_tab')

print("list")