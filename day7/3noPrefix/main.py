#!/bin/python3

import math
import os
import random
import re
import sys
import bisect

#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#
from itertools import combinations



def noPrefix(words):
    for i, word in enumerate(words):
        for j, word2 in enumerate(words):
            if i != j:
                if word2.startswith(word):
                    print(f"BAD SET\n{word}")
                    return
                if word.startswith(word2):
                    print(f"BAD SET\n{word2}")
                    return
    print("GOOD SET")


if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)
