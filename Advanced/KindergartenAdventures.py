import os
import sys

def solve(t):
    #finding the value for all student in diagonal and as the teacher proceed from position 0
    diagonals = [0] * len(t)
    values = [0] * len(t)
    for idx, t_val in enumerate(t):
        #update diagonals with teacher move
        diagonals[idx - t_val] += 1
        #update values with teacher movement and student value
        values[0] += int(t_val <= idx)
    for idx in range(1, len(t)):
        #updating values further with diagonals
        values[idx] = values[idx-1] - diagonals[idx - 1] + 1
    return values.index(max(values))+1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t_count = int(input())

    t = list(map(int, input().rstrip().split()))

    id = solve(t)

    fptr.write(str(id) + '\n')

    fptr.close()
