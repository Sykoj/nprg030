from shape import Shape 

class Square(Shape):
    
    def draw(self):
        return '...'

    def area(self):
        return 42

    def rotate(self):
        pass


square = Square()
print(square.draw())