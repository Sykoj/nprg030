class Counter:
    def __init__(self, low, high):
        self.current = low - 1
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current < self.high:
            return self.current
        raise StopIteration

numbers = [ 1, 2, 3 ]
range1 = enumerate(numbers)
range2 = enumerate(numbers)

for c in Counter(3, 9):
    print(c)