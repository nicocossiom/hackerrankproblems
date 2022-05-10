#!/bin/python3

import math
import os
import random
import re
import string
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#
from typing import List

alphabet = list("abcdefghijklmnopqrstuvwxyz")

def rotate_alphabet(k):
    k = k % 26
    return alphabet[k:] + alphabet[:k]


def caesarCipher(s, k):
    ret = ""
    new_alphabet = rotate_alphabet(k)
    for i, ch in enumerate(s):
        g_ch = ch.lower()
        if g_ch in alphabet:
            new_index = alphabet.index(g_ch)
            if ch.isupper():
                ret += new_alphabet[new_index].capitalize()
            else:
                ret += new_alphabet[new_index]
        else:
            ret += ch
    return ret


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
