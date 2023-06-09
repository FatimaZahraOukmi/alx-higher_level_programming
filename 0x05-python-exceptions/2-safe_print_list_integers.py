#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    numero = 0
    for idx in range(x):
        try:
            print("{:d}".format(my_list[idx]), end="")
            numero += 1
        except (ValueError, TypeError):
            idx += 1
            continue
    print("")
    return numero
