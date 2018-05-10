class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """

        if "\n" not in input and "\t" not in input:
            if "." in input:
                return len(input)
            return 0
        dirs = input.split("\n")
        count = 0
        path = dirs[0]
        maxLen = 0
        for dir in dirs[1:]:
            if not dir.startswith("\t"):
                dir = dir.replace("    ", "\t", 1)
                if not dir.startswith("\t"):
                    count = 0
                    path = dir
                    continue
            if count == dir.count("\t"):
                path = path.rsplit("/", 1)[0] + "/" + dir.replace("\t", "")
            if count > dir.count("\t"):
                dirLi = path.split("/", dir.count("\t"))
                dirLi.pop()
                path = "/".join(dirLi) + "/" + dir.replace("\t", "")
            if count < dir.count("\t"):
                path += "/" + dir.replace("\t", "")
            count = dir.count("\t")
            if "." in dir:
                plen = len(path)
                if path[0] == '/':
                    plen -= 1
                maxLen = max(maxLen, plen)

        return maxLen

