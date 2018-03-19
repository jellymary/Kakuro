from modules.utils.location import Location
from modules.utils.block import Block
from modules.kakuro import Kakuro


class Parser:
    @staticmethod
    def parse(raw_kakuro):
        kakuro = []
        size = None
        is_horizontal_line = None
        for line in raw_kakuro:
            line = line.rstrip('\n')
            info = line.split(' ')
            if info[0] == 'S':
                size = tuple(map(lambda x: int(x), info[1].split('x')))
            elif info[0] == 'H':
                is_horizontal_line = True
            elif info[0] == 'V':
                is_horizontal_line = False
            else:
                if is_horizontal_line is None:
                    raise Exception('value of "is_horizontal_line" is not assigned')
                block = Block(Location.parse(',', info[0]), int(info[1]), int(info[2]), is_horizontal_line)
                kakuro.append(block)
        if size is None:
            raise Exception('value of "size" is not assigned')
        return Kakuro(size, kakuro)
