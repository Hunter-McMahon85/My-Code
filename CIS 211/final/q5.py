"""
Hunter McMahon
CIS 211
final q5
squish
"""
import random


class Grid:
    def __init__(self, size: int):
        """
        initiator function for the grid function
        :param size: int that determines the size of the initial grid
        """
        self.size = size
        self.data = []
        for x in range(size):
            row_list = []
            for y in range(size):
                row_list.append(0)
            self.data.append(row_list)

    def set_value(self, i: int, j: int, val: int):
        """
        sets the value of a specified grid square
        :param i: column int (0-index)
        :param j: row int (0-index)
        :param val: value to insert
        :return: void just modifies self.data
        """
        self.data[j][i] = val

    def __str__(self) -> str:
        """
        string representation of the grid
        :return: string of the grid
        """
        grid_string = ""
        string_data = []
        for x in range(self.size):
            row_list = []
            for y in range(self.size):
                row_list.append(str(self.data[x][y]))
            string_data.append(row_list)
        for x in range(self.size):
            row_str = " ".join(string_data[x]) + '\n'
            grid_string += row_str
        return grid_string

    def squish(self, k: int):
        """
        squishes the grid into a smaller one
        :param k: the size for the new grid
        :return: void, just changes grid values
        """
        new_size = int(self.size / k)
        corners = []
        corn_1 = []
        corn_2 = []
        corn_3 = []
        corn_4 = []
        # top left
        for y in range(new_size):
            for x in range(new_size):
                corn_1.append(self.data[x][y])
        # top right
        for y in range(new_size):
            for x in range(new_size, self.size):
                corn_2.append(self.data[x][y])
        # bottom left
        for y in range(new_size, self.size):
            for x in range(new_size):
                corn_3.append(self.data[x][y])
        # bottom right
        for y in range(new_size, self.size):
            for x in range(new_size, self.size):
                corn_4.append(self.data[x][y])
        corners.append(sum(corn_1))
        corners.append(sum(corn_2))
        corners.append(sum(corn_3))
        corners.append(sum(corn_4))

        self.__init__(new_size)
        self.set_value(0, 0, corners[0])
        self.set_value(0, 1, corners[1])
        self.set_value(1, 0, corners[2])
        self.set_value(1, 1, corners[3])


# test output for the grid
if __name__ == '__main__':
    a = Grid(4)
    for i in range(4):
        for j in range(4):
            a.set_value(i, j, random.randint(0, 9))
    print(a)
    a.squish(2)
    print(a)
