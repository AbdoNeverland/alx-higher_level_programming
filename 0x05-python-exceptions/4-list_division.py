#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    r = []
    for i in range(list_length):
        try:
            d = my_list_1[i] / my_list_2[i]
            r.append(d)
        except TypeError:
            r.append(0)
            print("wrong type")
        except ZeroDivisionError:
            r.append(0)
            print("division by 0")
        except IndexError:
            r.append(0)
            print("out of range")
            break
        finally:
            ""
    return r
