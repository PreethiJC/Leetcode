def solution(A):
    # write your code in Python 3.6
    p = 1
    sumF = 0
    minVal = 2001
    totalSum = sum(A)
    for a in A:
        if p < len(A):
            sumF += a
            sumS = totalSum - sumF
            diff = abs(sumF - sumS)
            minVal = min(minVal, diff)
            p += 1
    return minVal

print solution([-10, -5, -3, -4, -5])