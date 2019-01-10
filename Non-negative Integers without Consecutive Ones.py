

def toBinList(num):
    blist = []
    while num!=0:
        blist.append(num&1)
        num = num >> 1
    return blist

def findIntegers(num):


    binList = toBinList(num)
    f = [1, 2]
    for i in range(2, len(binList)+1):
        f.append(f[i-1] + f[i-2])
    r = 0


    for i in range(len(binList)-1, -1, -1):
        if binList[i] == 1:
            r = r + f[i]
            if i < len(binList)-1 and binList[i+1] == 1:
                return r
    r = r + 1
    return r



#print(findIntegers(5))

def findIntegersA(num):
    """
    :type num: int
    :rtype: int
    """
    if not num:
        return 1
    if num < 3:
        return num + 1

    f = [0] * 32
    f[0], f[1] = 2, 3
    for i in range(2, 32):
        f[i] = f[i - 1] + f[i - 2] - 1

    res = 0
    i = 0
    pre = 0
    while num >= (1 << i):
        if num & (1 << i):
            if pre:
                res = f[i] + f[i - 1] - 2
            elif res > 0:
                res += (f[i] - 1)
            else:
                res += f[i]
        pre = num & (1 << i)
        i += 1
    return res

for i in range(8):
    print(i, findIntegersA(i), toBinList(i), findIntegers(i))
