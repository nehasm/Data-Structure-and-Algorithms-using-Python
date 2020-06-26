#reverse list from middle and swapping to parts
def reverseArray(a):
    size = len(a)
    part1=[]
    part2=[]
    if size%2==0:
        for i in range(0,int(size/2)):
            part1.append(a[i])
        part1=part1[::-1]
        for i in range(int(size/2),size):
          part2.append(a[i])
        part2=part2[::-1]
        part2.extend(part1)
    else:
      for i in range(0,int(size/2)):
        part1.append(a[i])
      part1=part1[::-1]
      for i in range(int(size/2),size):
        part2.append(a[i])
      part2=part2[::-1]
      part2.extend(part1)
    return part2

a=reverseArray([1,2,3,4])
print(a)