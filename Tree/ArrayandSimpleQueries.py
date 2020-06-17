from array import array

n, n_queries = map(int, input().split())
data = array('L', map(int, input().split()))
assert len(data) == n
for m in range(n_queries):
    t, i, j = map(int, input().split())
    if t == 1:
        aux1 = i-1
        aux2 = j - aux1
        data[:aux2], data[aux2:j] = data[aux1:j], data[:aux1]
    else:
        aux1 = i-1
        aux2 = aux1 + n - j
        data[aux1:aux2], data[aux2:] = data[j:], data[aux1:j]
print(abs(data[0] - data[-1]))
print(*data)
