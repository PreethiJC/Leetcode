def plusOne(self, digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    strNum = "".join(map(str, digits))
    num = int(strNum) + 1
    return map(int, str(num))