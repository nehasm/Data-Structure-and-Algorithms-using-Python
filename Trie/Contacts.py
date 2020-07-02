import sys
from collections import defaultdict

sys.stdin.readline()
trie = defaultdict(int)

for line in sys.stdin.readlines():
    opr, value = line.strip().split(' ')

    if opr == 'add':
        for i in range(1, len(value) + 1):
            key = value[0:i]
            trie[key] += 1
    elif opr == 'find':
        print(trie[value])
