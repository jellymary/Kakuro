from modules.utils.cell import Cell


class Block:
    def __init__(self, location, sum, length, is_horizontal):
        self._location = location
        self._sum = sum
        self.is_horizontal = is_horizontal
        self._cells = [None for i in range(length)]
        # может здесь создавать новую служебную клетку и складвать ее в массив?

    @property
    def sum(self):
        return self._sum

    @property
    def location(self):
        return self._location

    @property
    def value_cells(self):
        return self._cells[1:]

    def append_cell(self, new_cell):
        if not isinstance(new_cell, Cell):
            raise ValueError('the object is not an heir to the Cell class')
        for index in range(len(self._cells)):
            if self._cells[index] is None:
                self._cells[index] = new_cell
                break

    def get_known_values(self):
        return tuple([cell.values[0] for cell in self.value_cells if cell is not None and len(cell.values) == 1])

    def __len__(self):
        return len(self.value_cells)

    def __iter__(self):
        return iter(self._cells)

    def __getitem__(self, index):
        return self._cells[index]

    def __setitem__(self, index, value):
        self._cells[index] = value

    def __eq__(self, other):
        if isinstance(other, Block):
            return self.location == other.location and \
                   self.is_horizontal == other.is_horizontal
        raise TypeError("Type of value is not Block")

    def __ne__(self, other):
        return not (self == other)

    def __str__(self):
        return "{} block {} {} {} ".format("Horizontal" if self.is_horizontal else "Vertical",
                                           str(self.location),
                                           self.sum,
                                           len(self))
