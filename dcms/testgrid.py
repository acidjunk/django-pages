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
                result += 'x'
            result += '\n'

        return result


class Grid(object):
    height = 2
    width = 16

    def __init__(self):
        self._data = [[0 for x in range(self.width)] for x in range(self.height)]
        print(self._data)

    def __str__(self):
        result = ''
        for k in range(self.height):
            for i in range(self.width):
                result += '.'
            result += '\n'
        return result

    def is_place_able(self, cell):
        if (cell.horizontal_position + cell.horizontal_size) > self.width:
            return False
        else:
            return True

    def check_override(self, cell, save):
        objects_in_row = 0
        long_enough = False
        print('all',self._data)
        for row in self._data[cell.vertical_position]: #, range(cell.horizontal_position,
                                                             #cell.horizontal_position+cell.horizontal_size):
            print('row', row)
            for col in range(cell.horizontal_position,cell.horizontal_position+cell.horizontal_size):
                print('col',self._data[row][col])

                if self._data[row][col] == 0:
                    if objects_in_row == cell.horizontal_size:
                        long_enough = True
                        if save:
                            for colp in range(cell.horizontal_position, cell.horizontal_position+cell.horizontal_size):
                                col[colp] = 1
                    else:
                        objects_in_row += 1
                        # print(objects_in_row)
                else:
                    print("e1, 1", self._data[row][col])
                    pass

                #if col == [0]:
                    #if objects_in_row == cell.horizontal_size:
                       # long_enough = True
                        #if save:
                            #for colp in range(cell.horizontal_position, cell.horizontal_position+cell.horizontal_size):
                                #col[colp] = 1
                    #else:
                        #objects_in_row += 1
                        # print(objects_in_row)
                #else:
                    #print("e1, 1", col)
                    #pass

        return long_enough

    def check_for_free_space(self, cell):
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
        if self.is_place_able(cell):  # false = fits
            if self.check_override(cell, False):
                # fits...
                # TODO add specific location for cells? and not randomly assigned
                # cell fits, recall the function and save it.
                self.check_override(cell, True)

                pass
            else:
                print("cell overrides another")
        else:
            print("cell is too big")

    def move_cell(self, cell):
        if self.check_override(cell, False):
            if self.check_override(cell, False):
                # fits...
                # TODO add specific location for cells? and not randomly assigned
                # cell fits, recall the function and save it.
                self.check_override(cell, True)

        else:
            print("cell does not fit somewhere else")


# TODO, Tests....
if __name__ == '__main__':
    my_cell = GridCell(0, 0, 16, 1) # H - V / Hs - Vs
    my_grid = Grid()
    my_grid.add_cell(my_cell)
    print("grid should now be full")
    my_cell2 = GridCell(0, 0, 16, 1) # H - V / Hs - Vs
    my_grid.add_cell(my_cell2)
    print(my_grid)