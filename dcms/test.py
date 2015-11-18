class GridCell(object):
    def __init__(self, horizontal_position, vertical_position, horizontal_size, vertical_size):
        self.horizontal_size = horizontal_size
        self.vertical_size = vertical_size
        self.horizontal_position = horizontal_position
        self.vertical_position = vertical_position

        self.data = [[0 for x in range(self.horizontal_size)] for x in range(self.vertical_size)]

    def __str__(self):
        result=''
        for row in self.data:
            for col in row:
                result = result + 'x'
            result = result + '\n'

        return result

class Grid(object):
    height = 2
    width = 16

    def __init__(self):
        self._data = [[0 for x in range(self.height)] for x in range(self.width)]
        print(self._data)

    def __str__(self):
        result = ''
        for k in range(self.height):
            for i in range(self.width):
                result = result + '.'
            result = result + '\n'
        return result

    def check_size(self, cell):
        if (cell.horizontal_position + cell.horizontal_size) > self.width:
            return True
        else:
            return False

    def check_override(self, cell):
        objects_in_row = 0
        long_enough = False

        for row in self._data:
            for object in row:
                if row[object] == 0:
                    if objects_in_row == cell.horizontal_size:
                        long_enough = True
                    else:
                        objects_in_row = objects_in_row + 1

        return long_enough

    def check_for_free_space(self, cell):
        objects_in_row = 0
        free_spaces = []
        for row in self._data:
            for object in row:
                if row[object] == 0:
                    if objects_in_row == cell.horizontal_size:
                        free_spaces = free_spaces + row
                        objects_in_row = 0
                    else:
                        objects_in_row = objects_in_row + 1

        return free_spaces

    def add_cell(self, cell):
        # do stuff with self._data
        if self.check_size(cell) == False: #false = fits
            if self.check_override(cell) == True:
                #fits...
                self._data = self._data + [cell]
                pass
            else:
                print("cell overrides another")
        else:
            print("cell is too big")

if __name__ == '__main__':
    my_cell = GridCell(0, 0, 6, 1)
    print(my_cell)

    my_grid = Grid()
    print(my_grid)
    my_grid.add_cell(my_cell)