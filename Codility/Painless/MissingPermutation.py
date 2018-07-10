def solution(A):
    # write your code in Python 3.6
    setA = set(A)
    sumA = sum(setA)
    rng = len(A) * (len(A) + 1)/2
    if sumA == rng:
        return 1
    else:
        return 0

print solution([1, 4, 1])