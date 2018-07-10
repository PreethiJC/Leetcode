# def rotateImage(a):
#     n = len(a)
#     # for i in range(0, int(n/2) + 1):
#     #     for j in range(i, n-i):
#     #         # 0 0, 0 1
#     #         temp = a[i][j]
#     #         a[i][j] = a[n-1-i][j]
#     #         a[n-1-i][j] = a[n-1-i][n-1-j]
#     #         a[n-1-i][n-1-j] = a[i][n-1-j]
#     #         a[i][n-1-j] = temp
#     # return a
#
# print rotateImage([[1,2,3],
#  [4,5,6],
#  [7,8,9]])

def rotateMatrix(mat):
    # Consider all squares one by one
    N = len(mat)
    for x in range(0, int(N / 2)):

        # Consider elements in group
        # of 4 in current square
        for y in range(x, N - x - 1):
            # store current cell in temp variable
            temp = mat[x][y]

            # move values from right to top
            mat[x][y] = mat[y][N - 1 - x]

            # move values from bottom to right
            mat[y][N - 1 - x] = mat[N - 1 - x][N - 1 - y]

            # move values from left to bottom
            mat[N - 1 - x][N - 1 - y] = mat[N - 1 - y][x]

            # assign temp to left
            mat[N - 1 - y][x] = temp
    return mat

print rotateMatrix([[1,2,3],
 [4,5,6],
 [7,8,9]])