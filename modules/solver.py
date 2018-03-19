class Solver:
    @staticmethod
    def solve(kakuro, solutions_count):
        for block in kakuro.blocks:
            partitions = Solver.get_block_partitions(block)
            if len(partitions) == 1:
                partitions = partitions[0]
                for adjacent_block, cell in kakuro.find_all_adjacents_blocks(block):
                    adj_partitions = Solver.get_block_partitions(adjacent_block)
                    if len(adj_partitions) == 1:
                        adj_partitions = adj_partitions[0]
                        intersection = list(set(partitions) & set(adj_partitions))
                        if len(intersection) != 1:
                            raise ValueError('Oh no!... something went wrong')
                        cell.values = intersection
                        partitions = Solver.get_block_partitions(block)

    @staticmethod
    def get_block_partitions(block):
        return Solver.get_partitions(block.sum, len(block) - 1, *block.get_known_values())

    @staticmethod
    def get_partitions(number, count, *known_cells):
        partitions = []
        parts = [1 for x in range(count)]
        parts[0] = number - count + 1
        while (True):
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
