def maximalSquare(matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    if matrix == []:
        return 0
    r = 0

    m, n = len(matrix), len(matrix[0])
    dp = [[0]*n for i in range(m)]

    for i in range(m):
        if matrix[i][0] == '1':
            dp[i][0] = 1
            r = 1
    for i in range(n):
        if matrix[0][i] == '1':
            dp[0][i] = 1
            r = 1

    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    if r < dp[i][j]:
                        r = dp[i][j]
    #print(dp)
    return r*r


m1 = [[1,0,1,0,0],[1,0,1,1,1],[1,1,1,1,1],[1,0,0,1,0]]
m2 = [[1,0,1,0,0],[1,0,1,1,1],[1,1,1,1,1],[1,0,1,1,1]]

#print(maximalSquare(m1))
#print(maximalSquare(m2))

#print(maximalSquare([]))



m3 = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(maximalSquare(m3))
print(maximalSquare([["1"]]))
'''
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
'''
