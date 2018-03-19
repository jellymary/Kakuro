import argparse
import sys

from modules.opener import Opener
from modules.parser import Parser
from modules.solver import Solver


def parsing_arguments():
    parser = argparse.ArgumentParser(description='This program solves and generates various kakuros',
                                     epilog=get_recording_rules())
    # mode = parser.add_mutually_exclusive_group()
    #
    # group = mode.add_argument_group()

    solver_mode = parser.add_mutually_exclusive_group(required=True)
    solver_mode.add_argument('-n', '--name',
                             help='file name containing kakuro')
    solver_mode.add_argument('-r', '--record',
                             action='store_true',
                             help='kakuro recording from the command line')

    parser.add_argument('-c', '--count',
                        type=int,
                        default=-1,
                        help='count of solution')
    # mode.add_argument('-g', '--generation',
    #                   action='store_true',
    #                   help='kakuro generation')

    # return parser.parse_args()
    # return parser.parse_args(['-r'])
    return parser.parse_args(['-n', '1'])


def get_recording_rules():
    return 'Rules for entering kakuro: ' \
           '(1) the first line indicates the size (S NxM) ' \
           '(2) horizontal and vertical blocks are recorded separately'


if __name__ == "__main__":
    args = parsing_arguments()
    # print(args)
    if not args.record:
        raw_kakuro = Opener.open_file(args.name)
    else:
        raw_kakuro = []
        while True:
            line = ''.join(sys.stdin.readline())
            if line.rstrip('\n') == 'end':
                break
            raw_kakuro.append(line)

    kakuro = Parser.parse(raw_kakuro)
    # kakuro.print('Kakuro')
    Solver.solve(kakuro, args.count)
    kakuro.print('Solution')
