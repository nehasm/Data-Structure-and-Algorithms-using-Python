n = int(input())

string = ""
hist = []

for i in range(n):
    myinput = input().strip().split(' ')
    
    if myinput[0] == '1':
        hist.append(string)
        string = string + myinput[1]
    elif myinput[0] == '2':
        hist.append(string)
        delpos = int(myinput[1])
        mypos = len(string) - delpos
        string = string[0:mypos]
    elif myinput[0] == '3':
        mypos = int(myinput[1]) - 1
        print(string[mypos])
    else:
        string = hist.pop()