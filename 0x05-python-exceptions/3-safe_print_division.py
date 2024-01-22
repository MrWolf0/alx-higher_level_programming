#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except (TypeError, ZeroDivisionError):
        print("not allowed division by zero!")
        return None
    finally:
        print("Inside result: {}".format(result))
    return result
