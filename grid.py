class Grid:
    def __init__(self, cell_size=60):
        self.cell_size = cell_size
        self.num_rows = 8
        self.num_cols = 8
        self.reset()

    def reset(self):
        self.grid = [[0] * self.num_cols for _ in range(self.num_rows)]
        self.grid[0] = [3, 4, 5, 2, 1, 5, 4, 3]
        self.grid[1] = [6] * 8
        self.grid[self.num_rows-2] = [12] * 8
        self.grid[self.num_rows-1] = [9, 10, 11, 8, 7, 11, 10, 9] 

    def __getitem__(self, row):
        return self.grid[row]

