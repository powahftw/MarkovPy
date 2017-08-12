from collections import defaultdict
from random import choice

class MarkovPy():
    def __init__(self):
        self.nextransition = defaultdict(list)
        self.sourcetxt = ""
        self.words = []
        
    def morewords(self, txt):
        self.sourcetxt += txt
        self.words = txt.split()
        for index, element in enumerate(self.words[:-1]):        # Loop over the words, skipping the first one
            self.nextransition[element].append(self.words[index+1])   # For each word append the next element as the possible following element
            
    def random_wordgeneration(self, n):

        if not n or n < 0: return ""                        # Sanity check on the number of words to generate
        
        generated = ""
        
        randomword = choice(self.words)
        generated += " " + randomword
        n -= 1
        
        while n > 0:
            randomword = choice(self.nextransition[randomword])
            generated += " " + randomword
            n -= 1

        return generated
