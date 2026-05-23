import points
import time
import task_2_BST_AVL_and_list
import file

bst_create_t = []
bst_search_t = []
bst_delete_t = []
bst_h = []
tab = file.load_data("random_tab")

for n in points.points:

    data = tab[:n]
    bst = task_2_BST_AVL_and_list.BST()

    start = time.perf_counter()
    for i, x in enumerate(data, start=1):
        bst.insert(x)
        bst_h.append(bst.height())

    end = time.perf_counter()
    bst_create_t.append(end - start)

    start = time.perf_counter()
    search = bst.search
    for x in data:
        search(x)

    end = time.perf_counter()
    bst_search_t.append(end - start)

    start = time.perf_counter()
    sorted_data_desc = sorted(data, reverse=True)
    delete = bst.delete
    for x in sorted_data_desc:
        delete(x)

    end = time.perf_counter()
    bst_delete_t.append(end - start)

file.save_data("", 'bst_create_t', True)
for element in bst_create_t:
    file.save_data([element], 'bst_create_t')

file.save_data("", 'bst_search_t', True)
for element in bst_search_t:
    file.save_data([element], 'bst_search_t')

file.save_data("", 'bst_delete_t', True)
for element in bst_delete_t:
    file.save_data([element], 'bst_delete_t')


file.save_data("", 'bst_h', True)
i=1
for element in bst_h:
    if i in points.points:
        file.save_data([element], 'bst_h')
    i=i+1