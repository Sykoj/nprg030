from abc import abstractmethod, ABCMeta

class Shape(metaclass=ABCMeta):

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def rotate(self):
        pass