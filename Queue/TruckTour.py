import os
import sys

#
# Complete the truckTour function below.
def truckTour(p):
    fuel=0
    n=len(p)
    p_n=0
    i=p_n
    while i<n:
        fuel=fuel+p[i][0]-p[i][1]
        if fuel<0:
            p_n=p_n+1
            i=p_n
            fuel=0
        else:
            i+=1
    return p_n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + '\n')

    fptr.close()
