class Circle:
    def __init__(self, radius):

        self.radius = radius

    def calc_perimeter(self):
        return 2 * 3 * self.radius
    def calc_area(self):
        return 3 * self.radius ** 2
    def get_circle_info(self):
        print("Jest to koło o promieniu {}.".format(self.radius))


circle = Circle(4)
print("Obwód koła: ", circle.calc_perimeter())
print("Pole koła: ", circle.calc_area())
circle.get_circle_info()