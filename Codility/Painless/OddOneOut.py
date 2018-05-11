def solution(A):
    # write your code in Python 3.6
    if len(A) == 1:
        return A[0]
    val = 0
    for a in A:
        val ^= a
    return val

print solution([9, 3, 9, 3, 9, 7, 9])

