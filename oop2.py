# oop 2
class circle:
    def __init__(self, r):  # set up
        self.radius = r

        def area(self):
            return 22 / 7 * self.radius ** 2

        def perimeter(self):
            return 22 / 7 * self.radius * 2

        def print_details(self):
            print("radius is ", self.radius)
            print("area is", self.area())
            print("perimeter is", self.perimeter())

    def print_details(self):
        pass

    def area(self):
        pass


# objects==instance of a class
c1 = circle(10)
c2 = circle(20)
c3 = circle(30)

print(c1.area())
c1.print_details()

my_circles=[c1,c2,c3]