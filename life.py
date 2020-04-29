class Grid():
    @classmethod
    def parse(cls, input):
        alive_positions = set()
        for x, line in enumerate(input.split("\n")):
            for y, cell in enumerate(line):
                if cell == "#":
                    alive_positions.add((x, y))
        return cls(alive_positions, x + 1)

    def __init__(self, alive_positions, size):
        self._alive_positions = alive_positions
        self._size = size

    def is_alive(self, x, y):
        return (x, y) in self._alive_positions

    def next_state(self):
        alive_positions = set()
        for x in range(self._size):
            for y in range(self._size):
                if self._next_cell_liveness(x, y):
                    alive_positions.add((x, y))
        return Grid(alive_positions, self._size)

    def _next_cell_liveness(self, x, y):
        if self.is_alive(x, y) and self._alive_neighbors(x, y) in (2, 3):
            return True # Survival
        if not self.is_alive(x, y) and self._alive_neighbors(x, y) == 3:
            return True # Reproduction

        return False # underpop & overcrowding

    def _alive_neighbors(self, x, y):
        neighbors_positions = [(x-1, y-1), (x-1, y),  (x-1, y+1),
                               (x,   y-1),            (x,   y+1),
                               (x+1, y-1), (x+1, y),  (x+1, y+1)]
        return sum([1 for x, y in neighbors_positions if self.is_alive(x, y)])

    def __str__(self):
        lines = []
        for x in range(self._size):
            line = ["#" if self.is_alive(x, y) else "." for y in range(self._size)]
            lines.append("".join(line))
        return "\n".join(lines)
