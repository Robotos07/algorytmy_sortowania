import time
import file
import points
import task_2_BST_AVL_and_list

tab = file.load_data("random_tab")
avl_h = []
avl_hr = []

for n in points.points:

    data = tab[:n]
    avl = task_2_BST_AVL_and_list.AVLTree()
    local_heights = []

    start = time.perf_counter()
    for x in data:
        avl.insert(x)
        local_heights.append(avl.height())

    end = time.perf_counter()
    avl_hr.extend(local_heights)
    avl_h.append(avl.height())

file.save_data("", 'avl_hr', True)
i = 1
for h in avl_hr:
    if i in points.points:
        file.save_data([h], 'avl_hr')
    i = i + 1

file.save_data("", 'avl_h', True)
for h in avl_h:
    file.save_data([h], 'avl_h')