
print("hello")


#qsort
def dpirot(array2n):
    return 0


#hannuo move from a to c
def hannoi(n, a, b, c):
    if n == 1:
        print(n, a, c)
    else:
        hannoi(n-1, a, c, b)
        hannoi(1, a, b, c)
        hannoi(n-1, b, a, c)

    return 0
hannoi(5, 'a', 'b', 'c')