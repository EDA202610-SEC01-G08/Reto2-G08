def new_list():
    newlist = {
        'elements': [], 
        'size': 0
    }
    return newlist

def get_element(my_list, index):
    # Convert 1-based index to 0-based for underlying Python list
    return my_list['elements'][index - 1]

def is_present(my_list, element, cmp_function):
    size = my_list['size']
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list['elements'][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            # Return 1-based position to match the rest of the codebase
            return keypos + 1
    return -1

def add_first(my_list, element):
    my_list['elements'].insert(0, element)
    my_list['size'] += 1
    return my_list

def add_last(my_list, element):
    my_list['elements'].append(element)
    my_list['size'] += 1
    return my_list

def size(my_list):
    return my_list['size']

def first_element(my_list):
    return my_list['elements'][0]

def is_empty(my_list):
    return my_list['size'] == 0

def get_last_element(my_list):
    return my_list['elements'][-1]

def get_element(my_list, index):
    return my_list['elements'][index - 1]

def remove_first(my_list):
    if my_list['size'] > 0:
        removed_element = my_list['elements'].pop(0)
        my_list['size'] -= 1
        return removed_element
    else:
        raise IndexError("List is empty")

def remove_last(my_list):
    if my_list['size'] > 0:
        removed_element = my_list['elements'].pop()
        my_list['size'] -= 1
        return removed_element
    else:
        raise IndexError("List is empty")

def insert_element(my_list, element, index):
    if index < 1 or index > my_list['size'] + 1:
        raise IndexError("Index out of bounds")
    my_list['elements'].insert(index - 1, element)
    my_list['size'] += 1
    return my_list

def delete_element(my_list, index):
    if index < 1 or index > my_list['size']:
        raise IndexError("Index out of bounds")
    removed_element = my_list['elements'].pop(index - 1)
    my_list['size'] -= 1
    return my_list

def change_info(my_list, index, new_element):
    if index < 1 or index > my_list['size']:
        raise IndexError("Index out of bounds")
    my_list['elements'][index - 1] = new_element
    return my_list

def exchange(my_list, index1, index2):
    if index1 < 0 or index1 >= my_list['size'] or index2 < 0 or index2 >= my_list['size']:
        raise IndexError("Index out of bounds")
    my_list['elements'][index1], my_list['elements'][index2] = my_list['elements'][index2], my_list['elements'][index1]
    return my_list

def sub_list(my_list, start_index, end_index):
    if start_index < 0 or end_index > my_list['size'] or start_index > end_index:
        raise IndexError("Index out of bounds")
    new_sublist = {
        'elements': my_list['elements'][start_index:end_index],
        'size': end_index - start_index
    }
    return new_sublist

def iterator(my_list):
    """Yield elements from the list (preserves external 1-based semantics where callers expect elements)."""
    for elem in my_list['elements']:
        yield elem

def default_sort_criteria(element_1, element_2):
    is_sorted = False
    if element_1 < element_2:
        is_sorted = True
    return is_sorted

def shell_sort(my_list, sort_crit):
    n = my_list['size']
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = my_list['elements'][i]
            j = i
            while j >= gap and sort_crit(my_list['elements'][j - gap], temp) > 0:
                my_list['elements'][j] = my_list['elements'][j - gap]
                j -= gap
            my_list['elements'][j] = temp
        gap //= 2

    return my_list

def selection_sort(my_list, cmp_function=default_sort_criteria):
    """Se recorre la lista y se selecciona el elemento más pequeño y se intercambia con el primer elemento. Luego se selecciona el segundo elemento más pequeño y se intercambia con el segundo elemento, y así sucesivamente."""
    size = my_list['size']
    for i in range(size):
        min_index = i
        for j in range(i + 1, size):
            if cmp_function(my_list['elements'][j], my_list['elements'][min_index]):
                min_index = j
        exchange(my_list, i, min_index)
    return my_list

def insertion_sort(my_list,sort_crit):
    size = my_list['size']
    elements = my_list['elements']
    for i in range(1, size):
        key = elements[i]
        j = i - 1
        while j >= 0 and sort_crit(key, elements[j]):
            elements[j + 1] = elements[j]
            j -= 1
        elements[j + 1] = key
        
    return my_list
    

def merge_sort(my_list, sort_crit):
    if my_list['size'] > 1:
        mid = my_list['size'] // 2
        left_half = {
            'elements': my_list['elements'][:mid],
            'size': mid
        }
        right_half = {
            'elements': my_list['elements'][mid:],
            'size': my_list['size'] - mid
        }
        
        merge_sort(left_half, sort_crit)
        merge_sort(right_half, sort_crit)
        
        i = j = k = 0
        
        while i < left_half['size'] and j < right_half['size']:
            if sort_crit(left_half['elements'][i], right_half['elements'][j]):
                my_list['elements'][k] = left_half['elements'][i]
                i += 1
            else:
                my_list['elements'][k] = right_half['elements'][j]
                j += 1
            k += 1
        
        while i < left_half['size']:
            my_list['elements'][k] = left_half['elements'][i]
            i += 1
            k += 1
        
        while j < right_half['size']:
            my_list['elements'][k] = right_half['elements'][j]
            j += 1
            k += 1
            
    return my_list

def quick_sort(my_list, sort_crit):
    if my_list['size'] > 1:
        pivot = my_list['elements'][my_list['size'] // 2]
        left = {
            'elements': [x for x in my_list['elements'] if sort_crit(x, pivot) and x != pivot],
            'size': 0
        }
        right = {
            'elements': [x for x in my_list['elements'] if not sort_crit(x, pivot)],
            'size': 0
        }

        quick_sort(left, sort_crit)
        quick_sort(right, sort_crit)

        my_list['elements'] = left['elements'] + [pivot] + right['elements']
        my_list['size'] = len(my_list['elements'])

    return my_list