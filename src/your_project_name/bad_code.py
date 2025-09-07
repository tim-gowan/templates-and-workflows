# This file is intentionally bad to test the linter - expect bad responses

import sys
import os  # This is an unused import


def long_function_name(
    argument1,
    argument2,
    argument3,
    argument4,
    argument5,
    argument6,
    argument7,
    argument8,
    argument9,
):
    print("This function has too many arguments.")


def another_bad_function():
    unused_variable = 1
    a = 1
    b = 2
    if a == None:
        print("This is bad.")
    if b == True:
        print("This is also bad.")


def deeply_nested_function(a, b, c, d, e, f, g, h, i):
    if a:
        if b:
            if c:
                if d:
                    if e:
                        if f:
                            if g:
                                if h:
                                    if i:
                                        print("This is too deep.")


def function_with_no_docstring():
    pass


def function_with_side_effects(a, b):
    c = a + b  # This is a side effect
    return c


def main():
    long_function_name(1, 2, 3, 4, 5, 6, 7, 8, 9)
    another_bad_function()
    deeply_nested_function(1, 2, 3, 4, 5, 6, 7, 8, 9)
    function_with_no_docstring()
    function_with_side_effects(1, 2)
