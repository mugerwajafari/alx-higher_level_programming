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
                result.append(0)
            except ZeroDivisionError:
                print("division by 0")
                result.append(0)
            except (TypeError, ValueError):
                print("wrong type")
                result.append(0)
            finally:
                # Ensure the lists are long enough
                if len(my_list_1) < list_length or len(my_list_2) < list_length:
                    print("out of range")
                    break
    except IndexError:
        pass
    return result

# Example usage:
my_list_1 = [10, 20, 30, 40]
my_list_2 = [2, 5, 0, 10]
list_length = 5