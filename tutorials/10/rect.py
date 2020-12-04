# Třída rect pro úlohu P1M: Třída na obdélníky

class Rect:
    def __init__(self, p1, p2):
        if p1[0] > p2[0]:
            self.x1, self.x2 = p2[0], p1[0]
        else:
            self.x1, self.x2 = p1[0], p2[0]
        if p1[1] > p2[1]:
            self.y1, self.y2 = p2[1], p1[1]
        else:
            self.y1, self.y2 = p1[1], p2[1]

    def __repr__(self):
        return f"Rect(({self.x1},{self.y1}),({self.x2},{self.y2}))"

    def perimeter(self):
        """ Vrací obvod obdélníka """
        return 2*abs(self.x2 - self.x1) + 2*abs(self.y2 - self.y1)

    def area(self):
        """ Vrací obsah obdélníka """
        return abs(self.x2 - self.x1)*abs(self.y2 - self.y1)

    def __eq__(self, other):
        """ Test, zda mají obdélníky stejné vrcholy """
        return  self.x1 == other.x1 and \
                self.x2 == other.x2 and \
                self.y1 == other.y1 and \
                self.y2 == other.y2

    def __contains__(self, other):
        """ Test, zda je ten druhý obdélník obsažen v tomto """
        return  self.x1 <= other.x1 and \
                self.x2 >= other.x2 and \
                self.y1 <= other.y1 and \
                self.y2 >= other.y2

    def __and__(self, other):
        """ Průnik dvou obdélníků: pro prázdný průnik vrací něco, co má 
            alespoň jeden z rozměrů nulový """
        x1 = max(self.x1, other.x1)
        x2 = min(self.x2, other.x2)
        y1 = max(self.y1, other.y1)
        y2 = min(self.y2, other.y2)
        if x1 > x2 or y1 > y2:
            x2,y2=x1,y1
        return  Rect((x1,y1),(x2,y2))
