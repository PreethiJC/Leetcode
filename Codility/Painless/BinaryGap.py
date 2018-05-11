def solution(N):
    # write your code in Python 3.6
    binN = bin(N)[2:]
    count = maxVal = 0
    print(binN)
    for digit in binN:
        print type(digit)
        if digit is 0:
            count += 1
        else:
            maxVal = max(count, maxVal)
            count = 0
    return maxVal

print solution(15)