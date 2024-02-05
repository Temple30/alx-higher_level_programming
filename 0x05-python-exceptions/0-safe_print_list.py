#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            count += 1
    except IndexError:
        pass  # Catch IndexError when trying to access beyond the list length

    print()  # Print a new line after the elements
    return count
