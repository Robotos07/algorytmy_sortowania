import task_2_BST_AVL_and_list
import time
import file
import points

list_create_t = []
list_search_t = []
list_delete_t = []
tab = file.load_data("random_tab")

for n in points.points:

    data = tab[:n]

    linked_list = task_2_BST_AVL_and_list.SortedLinkedList()

    start = time.perf_counter()
    for x in data:
        linked_list.insert_sorted(x)

    end = time.perf_counter()
    list_create_t.append(end - start)

    start = time.perf_counter()
    for x in data:
        linked_list.search(x)

    end = time.perf_counter()
    list_search_t.append(end - start)

    start = time.perf_counter()
    while linked_list.head:
        linked_list.delete_first()

    end = time.perf_counter()
    list_delete_t.append(end - start)


file.save_data("", 'list_create_t', True)
for element in list_create_t:
    file.save_data([element], 'list_create_t')

file.save_data("", 'list_search_t', True)
for element in list_search_t:
    file.save_data([element], 'list_search_t')

file.save_data("", 'list_delete_t', True)
for element in list_delete_t:
    file.save_data([element], 'list_delete_t')