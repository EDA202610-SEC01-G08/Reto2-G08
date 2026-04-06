def new_list():
    newlist = {
        'first': None,
        'last': None,
        'size': 0
    }
    return newlist

def get_elemet(my_list, pos):
    searchpos = 0
    node = my_list['first']
    while searchpos < pos:
        node = node['next']
        searchpos += 1
    return node["info"]

def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list['first']
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp['info']) == 0:
            is_in_array = True
        else:
            temp = temp['next']
            count += 1
    if not is_in_array:
        count = -1
    return count

def add_first(my_list, element):
    new_node = {'info': element, 'next': None}
    if my_list['first'] is None:
        my_list['first'] = new_node
        my_list['last'] = new_node
    else:
        new_node['next'] = my_list['first']
        my_list['first'] = new_node
    my_list['size'] += 1
    return my_list

def add_last(my_list, element):
    new_node = {'info': element, 'next': None}
    if my_list['first'] is None:
        my_list['first'] = new_node
        my_list['last'] = new_node
    else:
        my_list['last']['next'] = new_node
        my_list['last'] = new_node
    my_list['size'] += 1
    return my_list

def size(my_list):
    return my_list['size']

def first_element(my_list):
    return my_list['first']['info']

def is_empty(my_list):
    return my_list['size'] == 0

def last_element(my_list):
    return my_list['last']['info']

def get_element(my_list, pos):
    searchpos = 1
    node = my_list['first']
    while searchpos < pos:
        node = node['next']
        searchpos += 1
    return node["info"]

def remove_first(my_list):
    if my_list['size'] > 0:
        removed_element = my_list['first']['info']
        my_list['first'] = my_list['first']['next']
        my_list['size'] -= 1
        if my_list['size'] == 0:
            my_list['last'] = None
        return removed_element
    else:
        raise IndexError("List is empty")

def remove_last(my_list):
    if my_list['size'] > 0:
        removed_element = my_list['last']['info']
        if my_list['size'] == 1:
            my_list['first'] = None
            my_list['last'] = None
        else:
            current_node = my_list['first']
            while current_node['next'] != my_list['last']:
                current_node = current_node['next']
            current_node['next'] = None
            my_list['last'] = current_node
        my_list['size'] -= 1
        return removed_element
    else:
        raise IndexError("List is empty")

def insert_element(my_list, element, index):
    if index < 0 or index >= my_list['size'] + 1:
        raise IndexError("Index out of bounds")
    new_node = {'info': element, 'next': None}
    if index == 0:
        new_node['next'] = my_list['first']
        my_list['first'] = new_node
        if my_list['size'] == 0:
            my_list['last'] = new_node
    else:
        current_node = my_list['first']
        for _ in range(1, index - 1):
            current_node = current_node['next']
        new_node['next'] = current_node['next']
        current_node['next'] = new_node
        if new_node['next'] is None:
            my_list['last'] = new_node
    my_list['size'] += 1
    return my_list

def delete_element(my_list, pos):
    if pos < 0 or pos >= my_list['size']:
        raise IndexError("Index out of bounds")
    if pos == 0:
        removed_element = my_list['first']['info']
        my_list['first'] = my_list['first']['next']
        if my_list['size'] == 1:
            my_list['last'] = None
    else:
        current_node = my_list['first']
        for _ in range(1, pos):
            current_node = current_node['next']
        removed_element = current_node['next']['info']
        current_node['next'] = current_node['next']['next']
        if current_node['next'] is None:
            my_list['last'] = current_node
    my_list['size'] -= 1
    return my_list

def change_info(my_list, pos, new_element):
    if pos < 0 or pos >= my_list['size']:
        raise IndexError("Index out of bounds")
    current_node = my_list['first']
    for _ in range(pos):
        current_node = current_node['next']
    current_node['info'] = new_element
    return my_list

def exchange(my_list, pos_1, pos_2):
    if pos_1 < 0 or pos_1 >= my_list['size'] or pos_2 < 0 or pos_2 >= my_list['size']:
        raise IndexError("Index out of bounds")
    if pos_1 == pos_2:
        return my_list
    node1 = my_list['first']
    for _ in range(pos_1):
        node1 = node1['next']
    node2 = my_list['first']
    for _ in range(pos_2):
        node2 = node2['next']
    node1['info'], node2['info'] = node2['info'], node1['info']
    return my_list

def sub_list(my_list,pos_i, num_elem):
    if pos_i < 0 or pos_i >= my_list['size'] or num_elem < 0 or (pos_i + num_elem) > my_list['size']:
        raise IndexError("Index out of bounds")
    sublist = new_list()
    current_node = my_list['first']
    for _ in range(pos_i):
        current_node = current_node['next']
    for _ in range(num_elem):
        add_last(sublist, current_node['info'])
        current_node = current_node['next']
    return sublist

def default_sort_criteria(element_1, element_2):
    is_sorted = False
    if element_1 < element_2:
        is_sorted = True
    return is_sorted

def selection_sort(my_list, cmp_function=default_sort_criteria):
    if my_list['size'] > 1:
        current_node = my_list['first']
        while current_node is not None:
            min_node = current_node
            next_node = current_node['next']
            while next_node is not None:
                if cmp_function(next_node['info'], min_node['info']):
                    min_node = next_node
                next_node = next_node['next']
            if min_node != current_node:
                current_node['info'], min_node['info'] = min_node['info'], current_node['info']
            current_node = current_node['next']
    return my_list

def insertion_sort(my_list, cmp_function=default_sort_criteria):
    if my_list['size'] > 1:
        sorted_list = new_list()
        current_node = my_list['first']
        while current_node is not None:
            insert_element(sorted_list, current_node['info'], 0)
            current_node = current_node['next']
        return selection_sort(sorted_list, cmp_function)
    return my_list

def shell_sort(my_list, cmp_function=default_sort_criteria):
    if my_list['size'] > 1:
        n = my_list['size']
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp_node = my_list['first']
                for _ in range(i):
                    temp_node = temp_node['next']
                temp_info = temp_node['info']
                j = i
                while j >= gap:
                    prev_node = my_list['first']
                    for _ in range(j - gap):
                        prev_node = prev_node['next']
                    if cmp_function(prev_node['info'], temp_info):
                        break
                    temp_node = prev_node
                    j -= gap
                temp_node['info'] = temp_info
            gap //= 2
    return my_list

def merge(my_list, left_list, right_list, cmp_function):
    my_list['first'] = None
    my_list['last'] = None
    my_list['size'] = 0
    
    left_node = left_list['first']
    right_node = right_list['first']
    
    while left_node is not None and right_node is not None:
        if cmp_function(left_node['info'], right_node['info']):
            add_last(my_list, left_node['info'])
            left_node = left_node['next']
        else:
            add_last(my_list, right_node['info'])
            right_node = right_node['next']
    
    while left_node is not None:
        add_last(my_list, left_node['info'])
        left_node = left_node['next']
    
    while right_node is not None:
        add_last(my_list, right_node['info'])
        right_node = right_node['next']

def merge_sort(my_list, cmp_function=default_sort_criteria):
    if my_list['size'] > 1:
        mid = my_list['size'] // 2
        left_list = sub_list(my_list, 0, mid)
        right_list = sub_list(my_list, mid, my_list['size'] - mid)
        merge_sort(left_list, cmp_function)
        merge_sort(right_list, cmp_function)
        merge(my_list, left_list, right_list, cmp_function)
    return my_list

def quick_sort(my_list, cmp_function=default_sort_criteria):
    if my_list['size'] > 1:
        pivot = my_list['first']['info']
        less = new_list()
        equal = new_list()
        greater = new_list()
        current_node = my_list['first']
        while current_node is not None:
            if current_node['info'] == pivot:
                add_last(equal, current_node['info'])
            elif cmp_function(current_node['info'], pivot):
                add_last(less, current_node['info'])
            else:
                add_last(greater, current_node['info'])
            current_node = current_node['next']
        quick_sort(less, cmp_function)
        quick_sort(greater, cmp_function)
        my_list['first'] = None
        my_list['size'] = 0
        current_node = less['first']
        while current_node is not None:
            add_last(my_list, current_node['info'])
            current_node = current_node['next']
        current_node = equal['first']
        while current_node is not None:
            add_last(my_list, current_node['info'])
            current_node = current_node['next']
        current_node = greater['first']
        while current_node is not None:
            add_last(my_list, current_node['info'])
            current_node = current_node['next']
    return my_list