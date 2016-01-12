# import unittest
# from testgrid import Grid, GridCell
#
#
# class MyTest(unittest.TestCase):
#     def test_full_grid(self):
#         my_cell = GridCell(0, 0, 16, 2)
#         my_grid = Grid()
#         my_grid.add_cell(my_cell)
#
#         errors = 0
#         for row in my_grid._data:
#             for col in row:
#                 if row[col] == 0:
#                     errors += 1
#
#         assert errors == 0
#
#     def test_empty_grid(self):
#         print("cell should be too wide")
#         my_cell = GridCell(0, 0, 30, 1)
#         my_grid = Grid()
#         my_grid.add_cell(my_cell)
#
#     def test_empty_grid_2_cells(self):
#         print("cell should fit")
#         my_cell = GridCell(0, 0, 14, 2)
#         my_grid = Grid()
#         my_grid.add_cell(my_cell)
#         print("cell shouldn't fit")
#         my_cell = GridCell(0, 0, 14, 2)
#         my_grid.add_cell(my_cell)
#
#
# if __name__ == '__main__':
#     unittest.main()