class Solver:
    @staticmethod
    def solve(kakuro, solutions_count):
        for i in range(10):
            for block in kakuro.blocks:
                partitions = Solver.get_block_partitions(block)
                if len(partitions) == 1:
                    partitions = partitions[0]
                    for cell in block.value_cells:
                        if len(cell.values) == 0:
                            Solver.assign(kakuro, cell, list(partitions))
                        else:
                            intersection = Solver._get_intersection(cell.values, partitions)
                            if len(intersection) == 0:
                                raise ValueError('kakuro does not have a solution')
                            Solver.assign(kakuro, cell, intersection)
                else:
                    Solver.update(block, kakuro)

    @staticmethod
    def assign(kakuro, current_cell, value):
        current_cell.values = value
        if len(value) == 1:
            for block in kakuro.blocks:
                if current_cell not in block.value_cells:
                    continue
                Solver.update(block, kakuro)

    @staticmethod
    def update(block, kakuro):
        partitions = Solver.get_block_partitions(block)
        empty_cell = []
        full_cell = []
        for current_cell in block.value_cells:
            if len(current_cell.values) != 0:
                partitions = Solver._get_intersection(current_cell.values, partitions)
                full_cell.append(current_cell)
            else:
                empty_cell.append(current_cell)
        if len(partitions) == 1:
            inter = Solver._get_intersection(partitions, full_cell[0].values)[0]
            if len(full_cell) == 1:
                # full_cell[0].values = inter
                Solver.assign(kakuro, full_cell[0], inter)
                for empty in empty_cell:
                    empty.values = [digit for digit in partitions[0] if digit != inter]
            # if len(empty_cell) == 1:
            #     empty_cell[0].values = inter


    @staticmethod
    def _get_intersection(partitions, adj_partitions):
        return [adj_parts
                for adj_parts in adj_partitions
                for parts in partitions
                for digit in parts
                if digit in adj_parts]

    @staticmethod
    def _get_difference(partitions, known_values):
        if not isinstance(partitions, str):
            raise ValueError()
        diff = [int(x) for x in partitions]
        for value in known_values:
            if value in diff:
                diff.remove(value)
        return diff

    @staticmethod
    def _add_residue(partitions, block):
        difference = Solver._get_difference(partitions, block.get_known_values())
        if difference is not None and len(difference) == 1:
            for cell in block.value_cells:
                if len(cell.values) == 0:
                    cell.values = difference[0]

    @staticmethod
    def get_block_partitions(block):
        return Solver.get_partitions(block.sum, len(block) - 1, *block.get_known_values())

    @staticmethod
    def get_partitions(number, count, *known_cells):
        partitions = []
        parts = [1 for i in range(count)]
        parts[0] = number - count + 1
        while True:
            Solver._append(parts, partitions, known_cells)
            while parts[1] < parts[0] - 1:
                parts[0] -= 1
                parts[1] += 1
                Solver._append(parts, partitions, known_cells)
            if count < 3:
                break
            index = 2
            s = parts[0] + parts[1] - 1
            while index < count and parts[index] >= parts[0] - 1:
                s += parts[index]
                index += 1
            if index == count:
                break
            parts[index] += 1
            temp = parts[index]
            index -= 1
            while index > 0:
                parts[index] = temp
                s -= temp
                index -= 1
            parts[0] = s
        return partitions

    @staticmethod
    def _is_repeating_part(partition):
        for i in range(len(partition)):
            part = partition[i]
            if part in (partition[:i] + partition[i + 1:]):
                return True
        return False

    @staticmethod
    def _append(parts, partitions, known_cells):
        # known_cells is int
        partition = []
        for value in known_cells:
            if value not in parts:
                return
        for x in parts:
            if not 0 < x < 10:
                return
            partition.append(str(x))
        partition = ''.join(partition)
        if not Solver._is_repeating_part(partition):
            partitions.append(partition)
