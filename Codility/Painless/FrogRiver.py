def solution(X, A):
    # setA = set(A)
    sumRng = X * (X+1)/2
    totalSum = sumRng
    setA = set()
    for a in A:
        if a not in setA:
            setA.add(a)
            totalSum -= a
        if totalSum == 0:
            return A.index(a)
    return -1



print solution(5, [1, 3, 1, 4, 2, 3, 5, 4])
print solution(2, [2, 2, 2, 2, 2])
print solution(3, [1, 3, 1, 3, 2, 1, 3])
