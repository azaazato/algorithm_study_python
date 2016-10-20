def getval(A, i, j, L, H):
    if (i < 0 or i >= L or j < 0 or j >= H):
        return 0
    else:
        return A[i][j]

def find_max_block(A, r, c, L, H, size, cntarr, maxsize):
    if (r >= L or c >= H):
        return
    cntarr[r][c] = True
    size += 1
    if (size > maxsize):
        maxsize = size
    directions = [[-1,0], [-1,-1], [0,-1], [1,-1], [1,0], [1,1], [0,1], [-1,1]]
    for direction in directions:
        new_i = r + direction[0]
        new_j = c + direction[1]
        val = getval(A, new_i, new_j, L, H)
        if (val > 0 and cntarr[new_i][new_j] is False):
            maxsize = find_max_block(A, new_i, new_j, L, H, size, cntarr, maxsize)
    cntarr[r][c] = False
    return maxsize

def get_max_ones(A, rmax, colmax):
    maxsize = 0
    size = 0
    cntarr = [[False for j in range(0,colmax)] for i in range(0,rmax) ]
    for i in range(0, rmax):
        for j in range(0, colmax):
            if (A[i][j] == 1):
                maxsize = find_max_block(A, i, j, L, H, size, cntarr, maxsize)
    return maxsize

if __name__ == '__main__':
    A = [
            [1, 1, 0, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 0, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [0, 1, 0, 1, 1]
        ]

    L = len(A)
    H = len(A[0])
    print(get_max_ones(A, L, H))
