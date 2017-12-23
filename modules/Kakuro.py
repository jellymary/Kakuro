from modules.utils.Cell import Cell
from modules.utils.Location import Location


class Kakuro:
    def __init__(self, size, blocks):
        self._size = size
        self._blocks = blocks
        for block in self._blocks:
            location = block.get_location()
            for cell in block:
                if location == Location(2, 2):
                    print("kd")
                is_service_block, values_block = self._get_content(block, location, cell)
                adjacent_block = self.find_adjacent_block(block, location)
                if adjacent_block is not None:
                    is_service_ab, values_ab = self._get_content(adjacent_block, location, cell)
                    if not (is_service_block ^ is_service_ab):
                        new_cell = Cell(is_service_ab, values_block + values_ab, location)
                    else:
                        raise ValueError("Something went wrong")
                    adjacent_block.set_cell(new_cell)
                else:
                    new_cell = Cell(is_service_block, values_block, location)
                block.set_cell(new_cell)
                location = location + (Location(1, 0) if block.is_horizontal else Location(0, 1))

    def find_adjacent_block(self, block, location):
        for adjacent_block in self._blocks:
            current_location = location
            while current_location.x >= 0 and current_location.y >= 0:
                if adjacent_block.get_location() == current_location and adjacent_block != block:
                    if current_location == location:
                        return adjacent_block
                current_location = current_location + Location(-1, 0) if not block.is_horizontal else Location(0, -1)

    def _get_content(self, block, location, cell):
        if location == block.get_location():
            is_service = True
            values = [block.get_sum()]
        else:
            is_service = False
            values = cell.get_values() if cell is not None else []
        return tuple([is_service, values])

    def get_field(self):
        field = self._get_empty_field()
        for block in self._blocks:
            for cell in block:
                x, y = cell.get_location().get_tuple()
                if field[y][x] == '#':
                    field[y][x] = ('\\' if cell.is_service else '|')\
                        .join(list(map(lambda value: str(value), cell.get_values())))
        return field

    def _get_empty_field(self):
        width, height = self._size
        field = []
        for y in range(height):
            lines = []
            for x in range(width):
                lines.append('#')
            field.append(lines)
        return field

    def __str__(self):
        field = self.get_field()
        lines = []
        for line in field:
            lines.append('\t'.join(line))
        return '\n'.join(lines)
