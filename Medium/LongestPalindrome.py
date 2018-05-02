def longestPalindrome(word):
    sub = word[:2]
    lngth = 0
    longestSub = ""
    if sub == sub[::-1]:
        lngth = len(sub)
    for letter in word[2:]:
        sub += letter
        if sub == sub[::-1]:
            if lngth < len(sub):
                lngth = len(sub)
                longestSub = sub
        else:
            sub = sub[1:]
            if sub == sub[::-1]:
                if lngth < len(sub):
                    lngth = len(sub)
                    longestSub = sub
    return longestSub

print(longestPalindrome("babaddab"))

