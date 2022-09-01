# Ted Lawson 8/1/22

from Node import Node
from LinkedList import LinkedList


def main():
    link1 = LinkedList()
    link1.add_begin(5)
    link1.add_begin(58)
    link1.add_begin(9)
    link1.add_end(1)
    link1.add_end(110)
    link1.add_after(7, 3)
    link1.print()
    return


if __name__ == '__main__':
    main()
