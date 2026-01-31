from mazegen.cell_class import Cell
import random



class Generator:
    def __init__(self, height, width, entry, exit, seed: int | None, perfect) -> None:
        self.height = height
        self.width = width
        self.grid = self.create_grid()
        self.entry = entry
        self.exit = exit
        self.seed = seed
        self.perfect = perfect


    def create_grid(self) ->list[list[Cell]]:
        rows = []
        columns = []

        for y in range(self.height):
            for x in range(self.width):
                cell_obj = Cell(x, y)
                rows.append(cell_obj)
            columns.append(rows)
            rows = []
        return columns


    def remove_walls(self, current: Cell, next: Cell, direction):
        reverse_directions = {"N": "S", "S": "N", "E": "W", "W": "E"}
        current.walls[direction] = False
        next.walls[reverse_directions[direction]] = False


    def get_allowed_neighbours(self, current: Cell) -> list[set]:
        allowed_neighbours = []
        directions = {"N": (0, -1), "S": (0, 1), "E": (1, 0), "W": (-1, 0)}

        for dirc, (bx, by) in directions.items():
            tx, ty = bx + current.x, by + current.y

            if (0 <= tx < len(self.grid[0]) and 0 <= ty < len(self.grid)):
                check_cell: Cell = self.grid[ty][tx]
                if check_cell.visite == False:
                    allowed_neighbours.append((check_cell, dirc))
        return allowed_neighbours


    def generate_a_maze(self, start_x: int = 0, start_y: int = 0):

        if self.seed is not None:
            random.seed(self.seed)
        
        start_point: Cell = self.grid[start_y][start_x]
        start_point.visite = True
        stack = []
        stack.append(start_point)

        while (stack):
            all_neighbours = self.get_allowed_neighbours(stack[-1])
            if all_neighbours:
                take_one, dirt = random.choice(all_neighbours)
                take_one.visite = True
                self.remove_walls(stack[-1], take_one, dirt)
                stack.append(take_one)
            else:
                stack.pop()

        if self.perfect is False:
            self.add_loops()






    def get_grid(self):
        return self.grid



    def print_maze(self):
        for y in range(self.height):

            top = ''
            for x in range(self.width):
                top += '+' + ('━━━' if self.grid[y][x].walls['N'] else '   ')
            print(top + '+')

            side = ''
            for x in range(self.width):
                side += '┃̇̇̇' if self.grid[y][x].walls['W'] else ' '
                if self.entry == (x, y):
                    side += 'EN '
                elif self.exit == (x, y):
                    side += ' EX'
                else:
                    side += '   '
            side += '┃̇̇̇'
            print(side)

        bottom = ''
        for x in range(self.width):
            bottom += '+' + ('━━━' if self.grid[self.height-1][x].walls['S'] else '   ')
        print(bottom + '+')






    # for non perfect grid
    def add_loops(self, probability: float = 0.1) -> None:
        directions = {
            "N": (0, -1),
            "S": (0, 1),
            "E": (1, 0),
            "W": (-1, 0),
        }

        for y in range(self.height):
            for x in range(self.width):
                cell = self.grid[y][x]

                for dirc, (dx, dy) in directions.items():
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        neighbour = self.grid[ny][nx]

                        if cell.walls[dirc] and random.random() < probability:
                            self.remove_walls(cell, neighbour, dirc)





    # utils
    # def _is_on_border(self, x: int, y: int) -> bool:
    #     return (
    #         x == 0
    #         or x == self.width - 1
    #         or y == 0
    #         or y == self.height - 1
    #     )

    # def open_entry(self) -> None:
    #     x, y = self.entry
    #     if not self._is_on_border(x, y):
    #         raise ValueError("ENTRY must be on the maze border")
    #     cell = self.grid[y][x]
    #     if x == 0:
    #         cell.walls["W"] = False
    #         return
    #     if x == self.width - 1:
    #         cell.walls["E"] = False
    #         return
    #     if y == 0:
    #         cell.walls["N"] = False
    #         return
    #     if y == self.height - 1:
    #         cell.walls["S"] = False
    #         return
    
    # def open_exit(self) -> None:
    #     x, y = self.exit
    #     cell = self.grid[y][x]      
    #     # Ensure the exit is on the border
    #     if not self._is_on_border(x, y):
    #         raise ValueError("EXIT must be on the maze border")     
    #     # Determine the exact border and open only that wall
    #     if x == 0:  # Left border
    #         cell.walls["W"] = False
    #     elif x == self.width - 1:  # Right border
    #         cell.walls["E"] = False
    #     elif y == 0:  # Top border
    #         cell.walls["N"] = False
    #     elif y == self.height - 1:  # Bottom border
    #         cell.walls["S"] = False
