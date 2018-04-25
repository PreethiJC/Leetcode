class Codec:

    def __init__(self):
        self.code = {}


    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        self.code[id(longUrl)] = longUrl
        return "http://tinyurl.com/" + str(id(longUrl))


    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.code.get(int(shortUrl.replace("http://tinyurl.com/", "")))

url = "https://leetcode.com/problems/design-tinyurl"
codec = Codec()
print(codec.decode(codec.encode(url)))