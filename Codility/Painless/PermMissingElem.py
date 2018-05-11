def solution(A):
    # write your code in Python 3.6
    if not A:
        return 1
    minVal = 1
    maxVal = max(A)
    sumRng = sum(range(minVal, (maxVal + 1)))
    if sumRng == sum(A):
        return maxVal + 1
    missEle = sumRng - sum(A)
    return missEle

print solution([1])