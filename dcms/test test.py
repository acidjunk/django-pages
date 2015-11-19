import unittest
import testgrid as test


class MyTest(unittest.TestCase):
    def test_vol_grid(self):
        my_cell = test.GridCell(0, 0, 16, 2)
        my_grid = test.Grid()
        my_grid.add_cell(my_cell)
        print("grid should now be full")
        my_cell = test.GridCell(0, 0, 16, 2)
        my_grid.add_cell(my_cell)

    def test_leeg_grid(self):
        print("cell should be too wide")
        my_cell = test.GridCell(0, 0, 30, 1)
        my_grid = test.Grid()
        my_grid.add_cell(my_cell)

    def test_leeg_grid_2_cellen(self):
        print("cell should fit")
        my_cell = test.GridCell(0, 0, 14, 2)
        my_grid = test.Grid()
        my_grid.add_cell(my_cell)
        print("cell shouldn't fit")
        my_cell = test.GridCell(0, 0, 14, 2)
        my_grid.add_cell(my_cell)


    # TODO, je maakt een grid aan wat al vol is en je probeert een cell te plaatsen
    # TODO, je maakt een grid aan dat leeg is en je probeert een te brede cell te plaatsen
    # TODO, je maakt een grid aan dat leeg is en je probeert een cell te plaatsen die past, direct daarna probeer je nog een cell te plaatsen die niet meer past

print("...")

if __name__ == '__main__':
    print("start")
    MyTest.test_vol_grid(unittest.defaultTestLoader)
