from numpy import random


def get(list_in: list,NumQuestion):
    # list_in: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list_out: list = []

    for index in range(1, NumQuestion+1):
        idx = random_id(list_in, list_out)
        list_out.append(idx)

    return list_out


def random_id(list_in: list, list_out: list):
    while True:
        idx = get_id(list_in)
        if idx not in list_out:
            return idx


def get_id(list_in: list):
    return random.choice(list_in)


#if _name_ == "_main_":
 #   print(get())