import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    def leftrotation(D,A):
        for i in range(D):
            first_element=a.pop(0)
            A.append(first_element)
        return A
    
    ans = leftrotation(d,a)
    print(' '.join(map(str,ans)))