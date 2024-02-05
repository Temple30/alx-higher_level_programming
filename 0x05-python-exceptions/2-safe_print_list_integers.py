#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count_integers = 0
    try:
        for i in range(x):
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end=' ')
                count_integers += 1
        print()  # New line after printing integers
    except IndexError:
        pass  # Ignore if index is out of range
    finally:
        return count_integers


my_list = [1, "two", 3, "four", 5]


result = safe_print_list_integers(my_list, 3)
print("Number of integers printed:", result)
