import math
import os
import random
import re
import sys

def matches(a,b):
    if (a=="{" and b=="}") or (a=="(" and b==")") or (a=="[" and b=="]"):
        return True
    else:
        return False
    
def isBalanced(s):
    stack=[]
    result="NO"
    for i in s:
        if i in ["[","{","("]:
            stack.append(i)
        else:
            if len(stack)==0:
                return "NO"
            else:
                b=stack.pop()
            if matches(b,i):
                result="YES"
            else:
                return "NO"
    if len(stack)==0:
        return result
    else:
        return "NO"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
