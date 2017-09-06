# MarkovPy
Generation of Random Text based on [Markov Chain](https://en.wikipedia.org/wiki/Markov_chain) transitions. The generations of words follow a probabilistic model. 

## Example of Usage


Let's try to feed it the [Python Zen](https://www.python.org/dev/peps/pep-0020/)

```python
if __name__ == "__main__":
    
    PATH = "sample.txt"
    
    with open(PATH, "r") as f:
        txt = f.read()
        
    test = MarkovPy(txt)
    print (test.random_wordgeneration(25))
   
   
   # one and preferably only one obvious at first unless you're dutch. 
   # now is better than nested.
   # complex is better than dense.
  
  
   # Formatted output
  
```

## Experimental Options

```python
DOUBLE_PUNCT = True 
```

Is an experimental option used to establish a correlation between words separated by punctuations symbols.

```python
"Hello, world"
```

In this case a possibile transition from the "Hello" state would bring use to "," or "world" with both 50% of chance to happen.



