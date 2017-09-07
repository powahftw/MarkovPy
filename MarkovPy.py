from collections import defaultdict
from random import choice
import re
import string

DOUBLE_PUNCT = False

class MarkovPy():
    def __init__(self, txt = ""):
        self.sourcetxt = ""
        self.words = []
        
        if txt:
            self.morewords(txt)
        
    def morewords(self, txt = ""):
        """
        Add text to the source material. Process the new list of words and the transitions dictionary
        Args:
        txt (String): Text to add to the source material
        """
        self.sourcetxt += " " + txt
        self.nextransition = defaultdict(list)
        self.words = re.findall(r"[\w']+|[.,!?;]", self.sourcetxt)    # Split word and punctuations symbols
        self.words = [x.lower() for x in self.words]                  # We store the words as their lowercase version
        for index, element in enumerate(self.words[:-1]):             # Loop over the words, skipping the last one
            self.nextransition[element].append(self.words[index+1])   # For each word append the next element as the possible following element
            
            # Experimental option: Chain together words separated by punctuations symbols.
            
            if DOUBLE_PUNCT:
               if self.words[index] not in string.punctuaction and self.words[index+1] in string.punctuation and index + 2 < len(self.words):
                    self.nextransition[element].append(self.words[index+2])
            
            
    def random_wordgeneration(self, n = 10):
        """
        Generate n random word by chosing randomly from the transitions dictionary
        Args:
        n (int): Numbers of words to generate.
        Returns:
        generated (string): A string containing the generated output.
        """
        if not self.words not n or n < 0: return ""                                  # Sanity check on the number of words to generate
        
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
