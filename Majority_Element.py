from typing import List
from collections import defaultdict



def majorityElement(n):
    d = {}
    n=[2,2,1,3,1,2]
    for v in n:

        if v in n:
            d[v] += 1
        else:
            d[v] = 1

    for key in d:
        if d[key] > len(n) // 2:
            return key

