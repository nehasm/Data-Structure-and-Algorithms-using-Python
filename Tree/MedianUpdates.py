from bisect import insort

def mutate(nums, o, n):
    if o == 'r':
        try:
            idx = nums.index(n)
        except:
            return False
        nums.pop(idx)
        if len(nums) == 0:
            return False
        return True
    elif o == 'a':
        insort(nums, n)
        return True


def calc_median(nums):
    l = len(nums)
    m = l // 2
    if bool(l % 2):
        return nums[m]
    else:
        val = (nums[m - 1] + nums[m]) / 2
        if isinstance(val, float) and val.is_integer():
            return int(val)
        return val


def median(a,x,l):
    li = []
    
    for i in range(l):
        operation = a[i]
        num = x[i]
        mut = mutate(li, operation, num)
        if not mut:
            print('Wrong!')
            continue
        print(calc_median(li))
    

N = int(input())
s = []
x = []
for i in range(0, N):
   tmp = input().strip().split(' ')
   a, b = [xx for xx in tmp]
   s.append(a)
   x.append(int(b))
median(s,x,N)