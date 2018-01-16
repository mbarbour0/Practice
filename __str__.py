class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern
        
    def __str__(self):
        result = []
        for i in self.pattern:
            if i == ".":
                result.append("dot")
            if i == "_":
                result.append("dash")
        return '-'.join(result)
    

class S(Letter):
    def __init__(self):
        pattern = ['.', '.', '.']
        super().__init__(pattern)
        
print(S())