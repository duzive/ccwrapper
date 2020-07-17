class CCError(Exception):
    
    __slots__ = ('text', 'error')
    
    def __init__(self, text, error):
        self.text = text
        self.error = error