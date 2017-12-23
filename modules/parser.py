from modules.utils.Location import Location
from modules.utils.Block import Block
from modules.Kakuro import Kakuro


class Parser:
    def parse(path):
        kakuro = []
        with open(str(path), 'r', encoding='UTF-8') as file:
            for line in file:
                line = line.rstrip('\n')
                info = line.split(' ')
                if info[0] == 'S':
                    size = tuple(map(lambda x: int(x), info[1].split('x')))
                elif info[0] == 'H':
                    is_horizontal_line = True
                elif info[0] == 'V':
                    is_horizontal_line = False
                else:
                    block = Block(Location.parse(',', info[0]), int(info[1]), int(info[2]), is_horizontal_line)
                    kakuro.append(block)
        return Kakuro(size, kakuro)
