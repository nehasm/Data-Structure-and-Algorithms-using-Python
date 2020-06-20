# Initializing two stacks
stackin, stackout = [], []

for i in range(int(input())):
    
    itr = list(map(int, input().split(" ")))
    itr_opr = itr[0]
    

    if itr_opr == 1:
        stackin.append(itr[1])

    if itr_opr == 2:
        # If stack_out is not empty then pop from it
        if stackout:
            stackout.pop()
            continue
        else:
            # Move everything to the out stack:
            while stackin:
                stackout.append(stackin.pop())
            stackout.pop()
            continue

    if itr_opr == 3:
        if not stackout:
            print(stackin[0])
        else:
            print(stackout[-1])