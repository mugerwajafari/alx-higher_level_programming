#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    try:
        for i in range(list_length):
            try:
                # Try to perform division element-wise
                division_result = my_list_1[i] / my_list_2[i]
                result.append(division_result)
            except IndexError:
                print("out of range")
                break
            except ZeroDivisionError:
                print("division by 0")
                result.append(0)
            except (TypeError, ValueError):
                print("wrong type")
                result.append(0)
    except IndexError:
        pass
    return result
