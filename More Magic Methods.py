class Song:
    def __init__(self, artist, title, length):
        self.artist = artist
        self.title = title
        self.length = length
        
    def __eq__(self, other):
        return self.length == other
    
    def __lt__(self, other):
        return int(self.length) < other
    
    def __gt__(self, other):
        return int(self.length) > other
    
    def __ge__(self, other):
        return self.length > other or self.length == other
    
    def __le__(self, other):
        return self.length < other or self.length == other