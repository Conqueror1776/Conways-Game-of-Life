from board import Board
import unittest

class TestBoard(unittest.TestCase):

    def test_check_neighbors(self):
        test = Board(1, 0)
        test.grid = [[1, 0, 1],[1, 0, 1],[0, 1, 0]]
        self.assertEqual(test.check_neighbors(1, 1), 5, "Check Neighbor does not work")

        test = Board(1, 0)
        test.grid = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
        self.assertEqual(test.check_neighbors(1, 1), 0, "Check Neighbor does not work")

    def test_update(self):
        test = Board(1, 0)
        test.grid = [[1, 0, 1],[1, 0, 1],[0, 1, 0]]
        test.rows = 3
        test.col = 3
        test.update_board_normal()
        print(test.grid)
        self.assertEqual(test.grid[1][1], 0, "update_board_normal() does not function")

    def test_update_again(self):
        test = Board(1, 0)
        test.grid = [[0, 0, 0],[0, 1, 0],[0, 0, 0]]
        test.rows = 3
        test.col = 3
        test.update_board_normal()
        self.assertEqual(test.grid[1][1], 0, "update_board_normal() does not function")

    def test_glider(self):
        test = Board(1, 0)
        test.grid = [[0, 1, 0, 0], [0, 0, 1, 0], [1, 1, 1, 0], [0, 0, 0, 0]]
        test.rows, test.col = (4, 4)
        test.update_board_normal()
        self.assertEqual(test.grid, [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 1, 0, 0]], "Glider not working")

if __name__ == "__main__":
    unittest.main()
