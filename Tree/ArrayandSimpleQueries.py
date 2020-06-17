from array import array

n, n_queries = map(int, input().split())
data_array = array('L', map(int, input().split()))
assert len(data_array) == n
for m in range(n_queries):
    t, i, j = map(int, input().split())
    if t == 1:
        a1 = i-1
        a2 = j - a1
        data_array[:a2], data_array[a2:j] = data_array[a1:j], data_array[:a1]
    else:
        a1 = i-1
        a2 = a1 + n - j
        data_array[a1:a2], data_array[a2:] = data_array[j:], data_array[a1:j]
print(abs(data_array[0] - data_array[-1]))
print(*data_array)
