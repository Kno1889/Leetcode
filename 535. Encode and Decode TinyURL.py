CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
TINYURL = "http://tinyurl.com/"

class Codec:

    def __init__(self):
        self.encode_map = {} # long:short
        self.decode_map = {} # short:long

    def get_mapping(self):
        encode = ""
        for i in range(6):
            encode += CHARS[random.randint(0, len(CHARS) - 1)]
        return encode

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl in self.encode_map:
            return self.encode_map[longUrl]
        
        shortUrl = TINYURL + self.get_mapping()
        self.encode_map[longUrl] = shortUrl        
        self.decode_map[shortUrl] = longUrl

        return shortUrl

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.decode_map[shortUrl]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))