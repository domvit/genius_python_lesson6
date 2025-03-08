class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * self.width + 2 * self.height

    def calculate_diagonal(self):
        return (self.width ** 2) + (self.height ** 2)


rectangle_1 = Rectangle(100, 200)
rectangle_2 = Rectangle(2, 500)

area_1 = rectangle_1.calculate_area()
area_2 = rectangle_2.calculate_area()

print(f"Rectangle 1 area: {area_1}")
print(f"Rectangle 2 area: {area_2}")
