class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Location):
            return Location(self.x + other.x, self.y + other.y)
        raise TypeError("Type of value is not Location")

    def __iadd__(self, other):
        if isinstance(other, Location):
            self = self + other
        else:
            raise TypeError("Type of value is not Location")

    def __sub__(self, other):
        if isinstance(other, Location):
            return Location(self.x - other.x, self.y - other.y)
        raise TypeError("Type of value is not Location")

    def __eq__(self, other):
        if isinstance(other, Location):
            return self.x == other.x and self.y == other.y

    def parse(sep, line):
        coordinate = line.split(sep)
        return Location(int(coordinate[0]), int(coordinate[1]))

    def get_tuple(self):
        return tuple([self.x, self.y])

    def __str__(self):
        return "({}, {})".format(self.x, self.y)
