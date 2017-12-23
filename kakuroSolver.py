from modules.parser import Parser
import os.path as path

class Kakuro_Solver:
    def solve(kakuro):
        pass


if __name__ == "__main__":
    try:
        kakuro_path = path.join('modules', 'fields', input())
        kakuro = Parser.parse(kakuro_path)
        print(kakuro)
        # Kakuro_Solver.solve(kakuro)
        # print(kakuro)
    except FileNotFoundError:
        print('invalid kakuro number')
