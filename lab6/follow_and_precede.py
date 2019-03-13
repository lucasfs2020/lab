# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 18:13:32 2019

@author: standl
"""

import gzip
from string import ascii_lowercase as lowercase

import itertools as it

lookup = dict((c, lowercase.index(c)) for c in lowercase)

def flatten(perm):
    flat = []
    for i in perm:
        for j in i:
            flat.append(''.join(j))
                
    return flat

def edit_distance_one(word):
    for i in range(len(word)):
        left, c, right = word[0:i], word[i], word[i + 1:]
        for cc in lowercase:
            yield it.permutations(left+cc+right, r=None)

#perm = it.permutations("hello", r=None)

#for i in list(perm):
#    print(i)
            
fh = gzip.open('words4_dat.txt.gz', 'r')
words = set()
for line in fh.readlines():
    line = line.decode()
    if line.startswith('*'):
        continue 
    else:
        w = str(line[0:4])
    words.add(w)

inp='what'

permu = edit_distance_one(inp)

perm_flat = flatten(permu)

follow_or_precede = []

for i in perm_flat:
    if i in words:
        follow_or_precede.append(i)

print("output for " + inp)
print(follow_or_precede)
#print((edit_distance_one("hello")))