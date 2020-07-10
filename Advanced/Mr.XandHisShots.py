import os
import sys

from bisect import bisect_left, bisect_right
    
def solve(shots, players):
    s_array, e_array = [], []
    for s in shots:
        i, j = s
        s_array.append(i)
        e_array.append(j)
    s_array.sort()
    e_array.sort()
    result = 0
    for p in players:
        i, j = p
        result += bisect_right(s_array, j) - bisect_left(e_array, i)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    shots = []

    for _ in range(n):
        shots.append(list(map(int, input().rstrip().split())))

    players = []

    for _ in range(m):
        players.append(list(map(int, input().rstrip().split())))

    result = solve(shots, players)

    fptr.write(str(result) + '\n')

    fptr.close()
