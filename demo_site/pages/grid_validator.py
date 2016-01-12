class GridCellValidator(object):
    def __init__(self, horizontal_position, vertical_position, horizontal_size, vertical_size):
        self.horizontal_size = horizontal_size
        self.vertical_size = vertical_size
        self.horizontal_position = horizontal_position
        self.vertical_position = vertical_position
        self.data = [[0 for _ in range(self.horizontal_size)] for _ in range(self.vertical_size)]

    def __str__(self):
        result = ''
        for row in self.data:
            for _ in row:
                result += 'x'
            result += '\n'

        return result


class GridValidator(object):
    height = 2
    width = 16

    def __init__(self):
        self._data = [[0 for _ in range(self.width)] for _ in range(self.height)]
        print(self._data)

    def __str__(self):
        result = ''
        for row in range(0, self.height):
            print('row', row)
            for col in range(0, self.width):
                print('col', self._data[row][col])
                if self._data[row][col] == 0:
                    result += '0'
                else:
                    result += '1'
            result += '\n'
        return result

    def is_place_able(self, cell):
        """ Checks if the width of the cell isn't wider then the grid
        :param cell: an instance of a grid cell
        """
        if (cell.horizontal_position + cell.horizontal_size) > self.width:
            return False
        else:
            return True

    def check_override(self, cell, save):
        """ Checks if the new cell doesn't override another cell on it's horizontal and vertical position and returns
        long_enough = true or false
        :param cell: an instance of a grid cell
        :param save: whenever to save the changes or not
        """
        objects_in_row = 0
        long_enough = False
        for row in self._data[cell.vertical_position]:
            print('row', row)
            for col in range(cell.horizontal_position, cell.horizontal_position+cell.horizontal_size):
                print('col', self._data[row][col])
                if self._data[row][col] == 0:
                    if objects_in_row == cell.horizontal_size:
                        long_enough = True
                        if save:
                            for colp in range(cell.horizontal_position, cell.horizontal_position+cell.horizontal_size):
                                self._data[row][colp] = 1
                    else:
                        objects_in_row += 1
                else:
                    pass
        return long_enough

    def remove_cell(self, cell, save):
        """
        removes the given cell and saves the changes
        :param cell: an instance of a grid cell
        :param save: whenever to save the changes or not
        :return: Validates if all the cells have been removed
        """
        objects_in_row = 0
        long_enough = False
        for row in self._data[cell.vertical_position]:
            for col in range(cell.horizontal_position, cell.horizontal_position+cell.horizontal_size):
                print('col', self._data[row][col])
                if self._data[row][col] == 1:
                    if objects_in_row == cell.horizontal_size:
                        long_enough = True
                        if save:
                            for colp in range(cell.horizontal_position, cell.horizontal_position+cell.horizontal_size):
                                self._data[row][colp] = 0
                    else:
                        objects_in_row += 1
                else:
                    print("e1, 1", self._data[row][col])
                    pass
        return long_enough

    def check_row_for_free_places(self, cell):
        """
        checks the given vertical row if the given cell location is free to use
        :param cell: an instance of a grid cell
        :return: returns the amount of chained free spaces
        """
        free_places = 0
        for row in self._data[cell.vertical_position]:
            for col in range(cell.horizontal_position, cell.horizontal_position+cell.horizontal_size):
                if self._data[row][col] == 0:
                        free_places += 1
                else:
                    pass
        return free_places

    def check_for_free_space(self, cell):
        """
        checks all vertical rows for free space
        :param cell: an instance of a grid cell
        :return: returns the amount of chained free spaces
        """
        objects_in_row = 0
        free_spaces = []
        for row in self._data:
            for col in range(cell.horizontal_position, cell.horizontal_position+cell.horizontal_size):
                if row[col] == 0:
                    if objects_in_row == cell.horizontal_size:
                        free_spaces += row
                        objects_in_row = 0
                    else:
                        objects_in_row += 1
        return free_spaces

    def add_cell(self, cell):
        """
        Method to check if a cell can be placed in the grid.
        :param cell: an instance of a grid cell
        :return: return True if cell is place able, False otherwise
        """
        if self.is_place_able(cell):  # false = fits
            if self.check_override(cell, False):
                self.check_override(cell, True)
                return True
            else:
                print("cell overrides another")
                return False
        else:
            print("cell is too wide")
            return False

    def move_cell(self, cell):
        """
        moves a cell to a new location
        :param cell: an instance of a grid cell
        :return: returns true if the cell was moved correctly, false if not
        """
        if self.check_override(cell, False):
            if self.remove_cell(cell, False):
                self.remove_cell(cell, True)
                self.add_cell(cell)
        else:
            return False
