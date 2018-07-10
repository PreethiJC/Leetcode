def solution(N, A):
    # write your code in Python 3.6
    # print A
    setA = set(A)
    if len(A) > 1 and len(setA) == 1:
        return [0] * N
    counter = [0] * N
    maxVal = 0
    for a in A:
        if a == N + 1:
            counter = [maxVal] * N
        else:
            counter[a-1] += 1
            maxVal = max(maxVal, counter[a-1])
    return counter

# print solution(5, [3, 4, 4, 6, 1, 4, 4])
# print(solution(5, [6, 6, 6, 6, 6, 6]))
# print(solution(5, [0, 0, 0, 0, 0, 6]))


print solution(1, [2]*1000)