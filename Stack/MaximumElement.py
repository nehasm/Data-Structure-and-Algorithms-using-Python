n = int(input().strip())
stack = []
stackmax = [0]

for i in range(n):

    q = list(map(int, input().strip().split(' ')))

    if q[0] == 1:

        stack.append(q[1])
        if q[1] >= stackmax[-1]:
            stackmax.append(q[1])

    elif q[0] == 2:

        if stack.pop() == stackmax[-1]:
            stackmax.pop()

    else:
        print (stackmax[-1])
