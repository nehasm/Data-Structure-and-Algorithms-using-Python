T = int(input().strip())
#maintain dictionary for every update and check dictionary for query
for _ in range(T):
    N,M = list(map(int,input().strip().split()))
    base = dict()
    for _ in range(M):
        instance = input().strip().split()
        if instance[0] == "UPDATE":
            x,y,z,w = [int(i) for i in instance[1:]]
            base[(x,y,z)] = w
        else: 
            query = [int(i) for i in instance[1:]]
            X,Y,Z = [range(query[i],query[i+3]+1) for i in range(3)]
            print(sum(base[(x,y,z)] for x,y,z in base if x in X and y in Y and z in Z))