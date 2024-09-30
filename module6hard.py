from math import pi


class Figures:
    sides_count = 0

    def __init__(self, color, *sides: int, filled=True):
        self.__color = [*color]
        if len([*sides]) == 1:
            self.__sides = [*sides] * self.sides_count
        elif len([*sides]) == self.sides_count:
            if isinstance(self, (Circle, Triangle)):
                self.__sides = [*sides]
            elif isinstance(self, Cube):
                if len(set([*sides])) == 1:
                    self.__sides = [*sides]
                else:
                    self.__sides = [1] * self.sides_count
        elif len([*sides]) != self.sides_count:
            self.__sides = [1] * self.sides_count
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b) is True:
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        for s in sides:
            if isinstance(s, int) and s == self.sides_count:
                return True
            else:
                return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len([new_sides]) == self.sides_count:
            self.__sides = [*new_sides]


class Circle(Figures):
    sides_count = 1
    __radius = None

    def get_radius(self):
        __radius = self.__sides[0] / (2 * pi)
        return __radius

    def get_square(self):
        return pi * self.__radius ** 2


class Triangle(Figures):
    sides_count = 3

    def get_square(self):
        a = self._Figures__sides[0]
        b = self._Figures__sides[1]
        c = self._Figures__sides[2]
        p = (a + b + c) / 2
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5


class Cube(Figures):
    sides_count = 12

    def get_volume(self):
        return self._Figures__sides[0] ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

# Проверка дополнительных вариантов создания объектов и методов (для треугольника и куба)
# - не работает при попытке передать аргумент 'filled' (оставил "на потом")
# triangle1 = Triangle((120, 120, 120), 4)
# triangle2 = Triangle((120, 120, 120), 3, 4, 5)
# print(triangle1.get_square())
# print(triangle2.get_square())
# print(len(triangle1))
# print(len(triangle2))
# cube2 = Cube((111, 111, 111), 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7)
# cube3 = Cube((222, 222, 222), 8)
# print(cube2.get_sides())
# print(cube2.get_color())
# print(cube2.get_volume())
# print(cube3.get_sides())
# print(cube3.get_color())
# print(cube3.get_volume())
# cube2.set_sides(8, 9, 10, 11, 7, 7, 7, 7, 7, 2, 3, 4)  # стороны куба разной длины - не изменится
# print(cube2.get_sides())
