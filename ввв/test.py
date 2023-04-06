a_dict = {'a': 1, 'b': 2, 'c': 5, 'd': 10, 'f': 11}
b_dict = {'e': 1, 'b': 3, 'a': 5, 'c': 10, 'h': 11}


def max_dct(a_dict: dict, b_dict: dict):
    new_dict = {}
    for i in a_dict:
        if i in b_dict and a_dict[i] > b_dict[i]:
            new_dict[i] = a_dict[i]
        elif i in b_dict and a_dict[i] < b_dict[i]:
            new_dict[i] = b_dict[i]
        elif i is not b_dict:
            new_dict[i] = a_dict[i]
    for i in b_dict:
        if i is not a_dict:
            new_dict[i] = b_dict[i]
    print(new_dict)


max_dct(a_dict, b_dict)


def sum_dct(a_dict: dict, b_dict: dict):
    new_dict = {}
    for i in a_dict:
        if i in b_dict:
            new_dict[i] = a_dict[i] + b_dict[i]
        elif i is not b_dict:
            new_dict[i] = a_dict[i]
    for i in b_dict:
        if i in a_dict:
            continue
        else:
            new_dict[i] = b_dict[i]
    print(new_dict)


sum_dct(a_dict, b_dict)

my_list = [9, 3, 5, 5, 2, 1, 8, 7]


def sort_list(var_list):
    var = 0
    for i in range(1, len(var_list)):
        if var_list[i - 1] > var_list[i]:
            var_list[i - 1], var_list[i] = var_list[i], var_list[i - 1]
            var += 1
        else:
            continue
    if var != 0:
        return sort_list(var_list)
    elif var == 0:
        return var_list


print(sort_list(my_list))

start_list = ['dgdgfh', 'njdj', 'djdjjduen']


def all_eq(start_list: list):
    new_list = []
    for i in start_list:
        if new_list == []:
            new_list.append(i)
        elif len(i) > len(new_list[0]):
            new_list[0] = i
    for i in start_list:
        if i in new_list:
            continue
        else:
            n_ = len(new_list[0]) - len(i)
            for n in range(n_):
                i = i + '_'
            new_list.append(i)
    return new_list


print(all_eq(start_list))
