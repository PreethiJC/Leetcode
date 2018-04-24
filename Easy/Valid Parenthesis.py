class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        closeArr = [')', '}', ']']
        openArr = ['(', '{', '[']
        paraDict = []
        for para in s:
            if para in openArr:
                paraDict.append(para)
            elif para in closeArr:
                if not paraDict:
                    return False
                if openArr.index(paraDict.pop()) != closeArr.index(para):
                    return False
        if paraDict:
            return False
        else:
            return True
