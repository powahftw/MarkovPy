import unittest

from markovpy import MarkovPy

class TestMarkov(unittest.TestCase):
    def test_empty(self):
        test = MarkovPy()
        self.assertTrue(not test.words)
        self.assertTrue(test.random_wordsgeneration() == "")
        test.morewords("is this the is")
        self.assertTrue(test.nextransition['is'], ['this'])
        self.assertTrue(test.nextransition['the'], ['is'])

    def test_punct_and_upper(self):
        test = MarkovPy("Hey! There")
        self.assertTrue(test.nextransition['hey'], ['!'])
        test.morewords("hey world")
        self.assertTrue(test.nextransition['hey'], ['!', 'world'])

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
        self.assertTrue(test.random_wordsgeneration(), "hi hi hi hi hi hi hi hi hi hi")
        self.assertTrue(test.random_wordsgeneration(12), "hi hi hi hi hi hi hi hi hi hi hi hi")


if __name__ == "__main__":
    unittest.main()
