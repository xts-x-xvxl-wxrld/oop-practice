class Square:
    def __init__(self, height, length):
        self.height = height
        self.length = length

    def area(self):
        return self.height * self.length


class Rectangle(Square):
    def area(self):
        return self.length * self.height

