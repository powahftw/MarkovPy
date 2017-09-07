from markovpy import MarkovPy

import unittest

class Markov(unittest.TestCase):
    def test_empty(self):
        test = MarkovPy()
        self.assertTrue(not test.words)
        self.assertTrue(test.random_wordgeneration() == "")

    def test_nextransition(self):
        test = MarkovPy("hello world hello worlds")
        self.assertTrue(test.nextransition['hello'], ['world', 'worlds'])
        test.morewords("bye")
        self.assertTrue(test.nextransition['worlds'], ['bye'])

    def test_more_words(self):
        test = MarkovPy("hello")
        self.assertTrue(test.words, ['hello'])
        test.morewords("world")
        self.assertTrue(test.words, ['hello', 'world'])

    def test_generation(self):
        test = MarkovPy("hi hi hi hi hi hi hi hi hi hi")
        self.assertTrue(test.random_wordgeneration(), "hi hi hi hi hi hi hi hi hi hi")
        self.assertTrue(test.random_wordgeneration(12), "hi hi hi hi hi hi hi hi hi hi hi hi")

if __name__ == "__main__":
    unittest.main()
