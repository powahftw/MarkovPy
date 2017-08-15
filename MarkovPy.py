from collections import defaultdict
from random import choice
import re
import string

DOUBLE_PUNCT = True

class MarkovPy():
    def __init__(self):
        self.nextransition = defaultdict(list)
        self.sourcetxt = ""
        self.words = []
        
    def morewords(self, txt = ""):
        self.sourcetxt += txt
        self.words = re.findall(r"[\w']+|[.,!?;]", self.sourcetxt)    # Split word and punctuations symbols
        self.words = [x.lower() for x in self.words]                  # We store the words as their lowercase version
        for index, element in enumerate(self.words[:-1]):             # Loop over the words, skipping the last one
            self.nextransition[element].append(self.words[index+1])   # For each word append the next element as the possible following element
            
            # Experimental option: Chain togheter words separated by punctuations symbols.
            
            if DOUBLE_PUNCT:
               if self.words[index+1] in string.punctuation and index + 2 < len(self.words):
                    self.nextransition[element].append(self.words[index+2])
            
            
    def random_wordgeneration(self, n = 10):

        if not n or n < 0: return ""                                  # Sanity check on the number of words to generate
        
        generated = ""
        
        randomword = choice(self.words)
        generated += " " + randomword
        n -= 1
        
        while n > 0:                                                  
            if self.nextransition[randomword]:                        # If a possibile next transition exist... 
                randomword = choice(self.nextransition[randomword])   
            else:                                                     # Else start over from a random words  
                randomword = choice(self.words)                       
            generated += " " + randomword
            n -= 1

        return generated
