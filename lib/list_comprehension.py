#!/usr/bin/env python3

def return_evens(num_list):
    # # returns an empty list if odd
    is_even = [n for n in num_list if n % 2 == 0]
    return (is_even)


def make_exclamation(sentence_list):
    add_exclamation = [item +
                       '!' for item in sentence_list if (len(item)) != 0]
    return add_exclamation
