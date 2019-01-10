def maxIncreaseKeepingSkyline(grid):
    if grid == []:
        return 0

    x = len(grid)
    y = len(grid[0])
    xskyline = []
    yskyline = []
    skylinegrid = [[0]*x for i in range(y)]
    r = 0
    for i in range(x):
        for j in range(y):
            skylinegrid[i][j] = min(max(grid[i]), max([grid[k][j] for k in range(y)]))
            r = r + skylinegrid[i][j] - grid[i][j]
    return r


grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
maxIncreaseKeepingSkyline(grid)

print(maxIncreaseKeepingSkyline(grid))
