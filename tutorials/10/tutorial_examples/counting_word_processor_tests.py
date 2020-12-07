from words import CountingWordProcessor
import unittest

class CountingWordProcessorTest(unittest.TestCase):

    def test_counts_corrently(self):
        # Arrange.
        countingWordProcessor = CountingWordProcessor()
        words = [ 'ahoj', 'jak', 'se', 'mas' ]

        # Act.
        for word in words:
            countingWordProcessor.process_word(word)

        # Assert.
        self.assertEqual(len(words), countingWordProcessor.counter)

    
if __name__ == '__main__':
    unittest.main()