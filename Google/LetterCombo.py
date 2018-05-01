class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        alphaList = []
        numPad = {"2": "abc", "3": "def",
                  "4": "ghi", "5": "jkl", "6": "mno",
                  "7": "pqrs", "8": "tuv", "9": "wxyz"}

        for num in digits:
            alphaList.append(list(numPad[num]))

        while len(alphaList) >= 2:
            alphaList.insert(0, [x+y for x in alphaList[0] for y in alphaList[1]])
            alphaList = alphaList[0:1] + alphaList[3:]

        return alphaList[0]


