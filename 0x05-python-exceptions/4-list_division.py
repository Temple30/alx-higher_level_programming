#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")

            element_1 = my_list_1[i]
            element_2 = my_list_2[i]

            if not (isinstance(element_1, (int, float)) and isinstance(element_2, (int, float))):
                raise TypeError("wrong type")

            if element_2 == 0:
                raise ZeroDivisionError("division by 0")

            division_result = element_1 / element_2
            result.append(division_result)

        except IndexError as e:
            print(f"Error: {e}")
            result.append(0)

        except TypeError as e:
            print(f"Error: {e}")

        except ZeroDivisionError as e:
            print(f"Error: {e}")
            result.append(0)

        finally:
            pass

    return result

# Example usage:
my_list_1 = [10, 20, 30]
my_list_2 = [2, 5, 0]
list_length = 5
result_list = list_division(my_list_1, my_list_2, list_length)
print(result_list)