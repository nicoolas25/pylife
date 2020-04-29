import life
import unittest

class TestLife(unittest.TestCase):

    def test_grid_initialization(self):
        input = self.grid("...",
                          ".#.",
                          "..#")
        assert life.Grid.parse(input)

    def test_access_position_liveness(self):
        input = self.grid("...",
                          "..#",
                          "...")
        grid = life.Grid.parse(input)
        self.assertTrue(grid.is_alive(1, 2))
        self.assertFalse(grid.is_alive(0, 0))

    def test_next_cell_state_when_underpopulation(self):
        input = self.grid("...",
                          ".#.",
                          "..#")
        grid = life.Grid.parse(input)
        self.assertFalse(grid._next_cell_liveness(1, 1))

    def test_next_cell_state_when_survival(self):
        input = self.grid("...",
                          "##.",
                          ".##")
        grid = life.Grid.parse(input)
        self.assertTrue(grid._next_cell_liveness(1, 1))

    def test_next_cell_state_when_overcrowding(self):
        input = self.grid("###",
                          "###",
                          "###")
        grid = life.Grid.parse(input)
        self.assertFalse(grid._next_cell_liveness(1, 1))

    def test_next_cell_state_when_reproduction(self):
        input = self.grid("...",
                          "#..",
                          ".##")
        grid = life.Grid.parse(input)
        self.assertTrue(grid._next_cell_liveness(1, 1))

    def test_next_cell_state_when_underpopulation_when_dead(self):
        input = self.grid("...",
                          "#..",
                          ".#.")
        grid = life.Grid.parse(input)
        self.assertFalse(grid._next_cell_liveness(1, 1))

    def test_underpopulation(self):
        input = self.grid("...",
                          ".#.",
                          "..#")
        grid = life.Grid.parse(input)
        expected_grid = self.grid("...",
                                  "...",
                                  "...")
        self.assertEquals(str(grid.next_state()), expected_grid)

    def test_survival(self):
        input = self.grid("...",
                          "##.",
                          ".##")
        grid = life.Grid.parse(input)
        expected_grid = self.grid("...",
                                  "###",
                                  "###")
        self.assertEquals(str(grid.next_state()), expected_grid)

    def test_overcrowding(self):
        input = self.grid("###",
                          "###",
                          "###")
        grid = life.Grid.parse(input)
        expected_grid = self.grid("#.#",
                                  "...",
                                  "#.#")
        self.assertEquals(str(grid.next_state()), expected_grid)

    def test_reproduction(self):
        input = self.grid("...",
                          "#..",
                          ".##")
        grid = life.Grid.parse(input)
        expected_grid = self.grid("...",
                                  ".#.",
                                  ".#.")
        self.assertEquals(str(grid.next_state()), expected_grid)

    def grid(self, *args):
        return "\n".join([f"{l}" for l in args])
