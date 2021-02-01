#!/usr/bin/env python3
import sys
from ccp.credit_card_processor import Ccp
from ccp.user import User


def main():
    ccp = Ccp()
    if len(sys.argv) > 1:
        file_names = sys.argv[1:]
        for file_name in file_names:
            try:
                this_file = open(file_name, "r")
                commands = this_file.readlines()
                ccp = Ccp()
                for command in commands:
                    ccp.process(command)
                ccp.print()
            except IOError as e:
                return str(e)

    else:
        for command in sys.stdin:
            ccp.process(command)
        ccp.print()


if __name__ == '__main__':
    main()
