from abc import ABCMeta, abstractmethod

class WordReader(metaclass=ABCMeta):
    
    '''
    Returns -1 if nothing to read.
    '''
    @abstractmethod
    def read_word(self):
        pass


class WordProcessor(metaclass=ABCMeta):
    
    @abstractmethod
    def process_word(self, word):
        pass

class CountingWordProcessor(WordProcessor):
    def __init__(self):
        self.counter = 0

    def process_word(self, word):
        self.counter += 1


class WordMain:
    def __init__(self, word_reader, word_processor):
        self.word_reader = word_reader
        self.word_processor = word_processor

    def main(self):
        word = self.word_reader.read_word()
        while word != -1:
            self.word_processor.process_word(word)
            word = self.word_reader.read_word()


class FileWordReader(WordReader):
    
    def __init__(self, file):
        pass

    def read_word(self):
        pass

