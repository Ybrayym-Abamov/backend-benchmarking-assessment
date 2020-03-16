#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Command line utility that accepts a word file and prints a dictionary of
anagrams for that file.

Module provides a function find_anagrams which can be used to do the same
for an arbitrary list of strings.
"""

import sys

# Your name here, and any other people/sources who helped.
# Give credit where credit is due.
__author__ = "Ybrayym Abamov"


# def alphabetize(string):
#     """Returns alphabetized version of the string"""
#     return "".join(sorted(string.lower()))


def find_anagrams(words):
    """
    Returns a dictionary with keys that are alphabetized words and values
    that are all words that, when alphabetized, match the key.
    Example:
    {'dgo': ['dog'], 'act': ['cat', 'act']}
    """
    dict_ = {}
    for word in words:
        if ''.join(sorted(word)) in dict_:
            dict_[''.join(sorted(word))] += [word]
        else:
            dict_[''.join(sorted(word))] = [word]
    return dict_


def main(args):
    # run find_anagrams() on first argument filename
    if len(args) < 1:
        print("Please specify a word file!")
        sys.exit(1)

    with open(args[0]) as f:
        words = f.read().split()
    anagram_dict = find_anagrams(words)
    for k, v in anagram_dict.items():
        print("{} : {}".format(k, v))


if __name__ == "__main__":
    main(sys.argv[1:])
