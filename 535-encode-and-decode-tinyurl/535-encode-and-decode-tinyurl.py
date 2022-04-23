import random

class Codec:
    
    def __init__(self):
        self.enc = {}
        self.dec = {}
        self.useful_fruitful_string = "asdfasd123456987"

    def encode(self, longUrl: str) -> str:
        while longUrl not in self.enc:
            shorting = "".join(random.choice(self.useful_fruitful_string) for _ in range(8) )
            if shorting not in self.enc:
                self.enc[longUrl]=shorting
                self.dec[shorting]=longUrl
        return "http://tinyurl.com/"+self.enc[longUrl]
        """Encodes a URL to a shortened URL.
        """
        
    def decode(self, shortUrl: str) -> str:
        return self.dec[shortUrl[-8:]]  
        """Decodes a shortened URL to its original URL.
        """
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))