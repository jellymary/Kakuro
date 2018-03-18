from modules.utils.cell import Cell
from modules.utils.location import Location


class Kakuro:
    CELL_WIDTH = 7
    SEP = ':'
    EMPTY_BLOCK = SEP * CELL_WIDTH

    def __init__(self, size, blocks):
        self._size = size
        self.blocks = blocks
        for block in self.blocks:
            location = block.location
            for cell in block:
                is_service_block, values_block = Kakuro._get_content(block, location, cell)
                adjacent_block = self.find_adjacent_block(block, location)
                if adjacent_block is not None:
                    is_service_ab, values_ab = Kakuro._get_content(adjacent_block, location, cell)
                    if not (is_service_block ^ is_service_ab):
                        new_cell = Cell(is_service_ab, values_block + values_ab, location)
                    else:
                        raise ValueError("Something went wrong")
                    adjacent_block.append_cell(new_cell)
                else:
                    new_cell = Cell(is_service_block, values_block, location)
                block.append_cell(new_cell)
                location = location + (Location(1, 0) if block.is_horizontal else Location(0, 1))

    def find_adjacent_block(self, block, location):
        for adjacent_block in self.blocks:
            current_location = location
            while current_location.x >= 0 and current_location.y >= 0:
                if adjacent_block.location == current_location and adjacent_block != block:
                    if current_location == location:
                        return adjacent_block
                current_location = current_location + Location(-1, 0) if not block.is_horizontal else Location(0, -1)

    def find_all_adjacents_blocks(self, block):
        return [(self.find_adjacent_block(block, cell.location), cell) for cell in block.value_cells]

    @staticmethod
    def _get_content(block, location, cell):
        if location == block.location:
            is_service = True
            values = [block.sum]
        else:
            is_service = False
            values = cell.values if cell is not None else []
        return tuple([is_service, values])

    def get_field(self):
        field = self._get_empty_field()
        for block in self.blocks:
            for cell in block:
                x, y = cell.location.get_tuple()
                if field[y][x] == Kakuro.EMPTY_BLOCK:
                    field[y][x] = ('\\' if cell.is_service else '|')\
                        .join(list(map(lambda value: str(value), cell.values)))\
                        .center(Kakuro.CELL_WIDTH, Kakuro.SEP if cell.is_service else ' ')
        return field

    def _get_empty_field(self):
        width, height = self._size
        field = []
        for y in range(height):
            lines = []
            for x in range(width):
                lines.append(Kakuro.EMPTY_BLOCK)
            field.append(lines)
        return field

    def __str__(self):
        field = self.get_field()
        lines = []
        for line in field:
            lines.append('|'.join([x.center(Kakuro.CELL_WIDTH) for x in line]))
        return '\n'.join(lines)
