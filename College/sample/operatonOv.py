class squares:
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length ** 2
    def __lt__(self, other):
        return self.area() < other.area()
    def __gt__(self, other):
        return self.area() > other.area()
    def __eq__(self, other):
        return self.area() == other.area()
    def __le__(self, other):
        return self.area() <= other.area()
    def __ge__(self, other):
        return self.area() >= other.area()
    def __ne__(self, other):
        return self.area() != other.area()
    def __add__(self, other):
        return self.area() + other.area()
    def __sub__(self, other):
        return self.area() - other.area()
    def __mul__(self, other):
        return self.area() * other.area()
    def __truediv__(self, other):
        return self.area() / other.area()
object1 = squares(5)
object2 = squares(6)
print(object1.__add__(object2))
print(object1 < object2)
print(object1 > object2)
print(object1 == object2)
print(object1 <= object2)
print(object1 >= object2)
print(object1 != object2)
print(object1 + object2)
print(object1 - object2)
print(object1 * object2)
print(object1 / object2)
