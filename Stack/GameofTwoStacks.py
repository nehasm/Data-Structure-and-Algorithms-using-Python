import sys

g = int(input().strip())
for a0 in range(g):
    n,m,x = input().strip().split(' ')
    n,m,x = [int(n),int(m),int(x)]
    a = list(map(int, reversed(input().strip().split(' '))))
    b = list(map(int, reversed(input().strip().split(' '))))

    total = 0
    atmp = []
    for i in range(n):
        val = a.pop()
        if total + val > x:
            break
        total += val 
        atmp.append(val)

    max_count = len(atmp)
    cur_count = max_count
    while m:
        if total + b[-1] <= x:
            total += b.pop() 
            m -= 1
            cur_count += 1
            if cur_count > max_count:
                max_count = cur_count
            continue
        if not len(atmp):
            break
        aval = atmp.pop()
        total -= aval
        cur_count -= 1
    print (max_count)
