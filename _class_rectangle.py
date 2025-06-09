class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        return isinstance(other, Rectangle) and self.get_square() == other.get_square()

    def __add__(self, other):
        if not isinstance(other, Rectangle):
            raise TypeError("You can only add rectangles.")
        total_area = self.get_square() + other.get_square()
        for w in range(int(total_area**0.5), 0, -1):
            if total_area % w == 0:
                h = total_area // w
                return Rectangle(w, h)

    def __mul__(self, n):
        if not isinstance(n, (int, float)):
            raise TypeError("You can only multiply by a number.")
        new_area = int(self.get_square() * n)
        for w in range(int(new_area**0.5), 0, -1):
            if new_area % w == 0:
                h = new_area // w
                return Rectangle(w, h)

    def __str__(self):
        return f"Rectangle({self.width}x{self.height}) - area: {self.get_square()}"


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, "Test1"
assert r2.get_square() == 18, "Test2"

r3 = r1 + r2
assert r3.get_square() == 26, "Test3"

r4 = r1 * 4
assert r4.get_square() == 32, "Test4"

assert Rectangle(3, 6) == Rectangle(2, 9), "Test5"
