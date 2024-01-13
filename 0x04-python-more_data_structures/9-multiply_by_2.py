#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # using map function to execute lambda expression
    # over the dic .
    # lambda use the item [0] which consist the key
    # item[1] which consist the value then *2
    # finally return a dict
    return dict(map(lambda item: (item[0], item[1] * 2), a_dictionary.items()))
