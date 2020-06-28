#Intially making every node as item in dict and then merging them with commands.
#for Q checking the length in main dictionary
N, Q = tuple(map(int, input().split(' ')))

dict1 = dict()
dict2 = dict()

for i in range(N):
    dict1[i] = str(i)
    dict2[str(i)] = [i]

for q in range(Q):
    command = input().split(' ')
    if command[0] == 'Q':
        I = int(command[1]) - 1
        community = dict1[I]
        print(len(dict2[community]))
    else:
        I, J = int(command[1]) - 1, int(command[2]) - 1
        com1, com2 = dict1[I], dict1[J]
        if com1 != com2:
            x, y = dict2[com1], dict2[com2]
            if len(x) > len(y):
                x, y = y, x
                com1, com2 = com2, com1
            for k in x:
                dict1[k] = com2
            y.extend(x)
            del dict2[com1]