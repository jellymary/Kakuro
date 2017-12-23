from modules.utils.Cell import Cell


class Block:
    def __init__(self, location, sum, length, is_horizontal):
        self._location = location
        self._sum = sum
        self._length = length
        self.is_horizontal = is_horizontal
        self._cells = []
        for i in range(length):
            self._cells.append(None)

    def get_sum(self):
        return self._sum

    def get_location(self):
        return self._location

    def set_cell(self, new_cell):
        for index in range(len(self._cells)):
            if self._cells[index] is None:
                self._cells[index] = new_cell
                break

    def __len__(self):
        return self._length

    def __iter__(self):
        return iter(self._cells)

    def __getitem__(self, index):
        return self._cells[index]

    def __setitem__(self, key, value):
        self._cells[key] = value

    def __eq__(self, other):
        if isinstance(other, Block):
            return self._location == other.get_location() and \
                   self.is_horizontal == other.is_horizontal
        raise TypeError("Type of value is not Block")

    def __ne__(self, other):
        return not (self == other)

    def __str__(self):
        return "{} block {} {} {} ".format("Horizontal" if self._is_horizontal else "Vertical",
                                           str(self._location),
                                           self._sum,
                                           self._length)
