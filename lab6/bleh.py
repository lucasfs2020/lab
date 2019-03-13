# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 16:40:13 2019

@author: standl
"""

import itertools as it
from string import ascii_lowercase as lowercase

lookup = dict((c, lowercase.index(c)) for c in lowercase)

def flat(permu):
    flatt = []
    for i in edit_distance_one("hello"):
        for j in i:
            flatt.append(''.join(j))
    
    return flatt

def edit_distance_one(word):
    for i in range(len(word)):
        left, c, right = word[0:i], word[i], word[i + 1:]
        j = lookup[c]  # lowercase.index(c)
        for cc in lowercase[j + 1:]:
            yield (it.permutations(left+cc+right, r=None))

#perm = it.permutations("hello", r=None)

#for i in list(perm):
#    print(i)

perm = edit_distance_one("hello")

print(perm)

flat_boy = flat(perm)

for i in flat_boy:
    print(i)
#print((edit_distance_one("hello")))