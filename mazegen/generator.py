from mazegen.cell_class import Cell
import random


RESET = "\033[0m"
RED   = "\033[31m"
GREEN = "\033[32m"
YELLOW= "\033[33m"
BLUE  = "\033[34m"
MAGENTA = "\033[35m"
CYAN  = "\033[36m"
WHITE = "\033[37m"


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
    

    def get_allowed_neighbours(self, current: Cell) -> list[tuple]:
        allowed_neighbours = []
        directions = {"N": (0, -1), "S": (0, 1), "E": (1, 0), "W": (-1, 0)}

        for dirc, (bx, by) in directions.items():
            tx, ty = bx + current.x, by + current.y

            if (0 <= tx < len(self.grid[0]) and 0 <= ty < len(self.grid)):
                check_cell: Cell = self.grid[ty][tx]
                if check_cell.visited == False:
                    allowed_neighbours.append((check_cell, dirc))
        return allowed_neighbours


    def generate_a_maze(self, start_x: int = 0, start_y: int = 0):

        #check if enter and exit true:
        
        # if not (0 <= self.entry[0] < self.width and 0 <= self.entry[1] < self.height):
        #     raise ValueError(f"ENTRY coordinates {self.entry} are out of bounds")
    
        # if not (0 <= self.exit[0] < self.width and 0 <= self.exit[1] < self.height):
        #     raise ValueError(f"EXIT coordinates {self.exit} are out of bounds")

        # if self.entry == self.exit:
        #     raise ValueError("ENTRY and EXIT cannot be the same cell")

        # if not (self._is_on_border(*self.entry)):
        #     raise ValueError(f"ENTRY {self.entry} must be on the maze border")

        # if not (self._is_on_border(*self.exit)):
        #     raise ValueError(f"EXIT {self.exit} must be on the maze border")
        
        
        if self.seed is not None:
            random.seed(self.seed)
        
        start_point: Cell = self.grid[start_y][start_x]
        start_point.visited = True
        stack = []
        stack.append(start_point)

        while (stack):
            all_neighbours = self.get_allowed_neighbours(stack[-1])
            if all_neighbours:
                take_one, dirt = random.choice(all_neighbours)
                take_one.visited = True
                self.remove_walls(stack[-1], take_one, dirt)
                stack.append(take_one)
            else:
                stack.pop()

        if self.perfect is False:
            self.add_loops()
            
            
            
        # أغلق كل الحدود الخارجية
        self.close_external_borders()

        self.open_external_wall(self.entry)
        self.open_external_wall(self.exit)



    def get_grid(self):
        return self.grid





    def print_maze(self, show_path: bool = False, path_coords: list[tuple[int,int]] = None, color: str = "\033[36m"):
        CYAN  = "\033[36m"

        for y in range(self.height):
            top = ''
            for x in range(self.width):
                top += '+' + (color + '━━━' + RESET if self.grid[y][x].walls['N'] else '   ')
            print(top + '+')

            side = ''
            for x in range(self.width):
                side += color + '┃' + RESET if self.grid[y][x].walls['W'] else ' '
                if (x, y) == self.entry:
                    side += RED + 'EN ' + RESET
                elif (x, y) == self.exit:
                    side += RED + 'EX ' + RESET
                elif show_path and path_coords and (x, y) in path_coords:
                    side += RED + ' * ' + RESET
                else:
                    side += '   '
            side += color + '┃' + RESET
            print(side)

        bottom = ''
        for x in range(self.width):
            bottom += '+' + (color + '━━━' + RESET if self.grid[self.height-1][x].walls['S'] else '   ')
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
    def _is_on_border(self, x: int, y: int) -> bool:
        return (
            x == 0
            or x == self.width - 1
            or y == 0
            or y == self.height - 1
        )
    def open_external_wall(self, position: tuple[int, int]) -> None:
        x, y = position
        cell = self.grid[y][x]
    
        if not self._is_on_border(x, y):
            raise ValueError("ENTRY and EXIT must be on the maze border")
    
        # corners → choose vertical first
        if y == 0:
            cell.walls["N"] = False
        elif y == self.height - 1:
            cell.walls["S"] = False
        elif x == 0:
            cell.walls["W"] = False
        elif x == self.width - 1:
            cell.walls["E"] = False
    
    
    
    
    
    
    
    def close_external_borders(self) -> None:
        """
        تأكد أن كل الحدود الخارجية للمتاهة مغلقة ما عدا ENTRY و EXIT
        """
        for x in range(self.width):
            # الصف العلوي
            if (x, 0) != self.entry:
                self.grid[0][x].walls["N"] = True
            # الصف السفلي
            if (x, self.height - 1) != self.exit:
                self.grid[self.height - 1][x].walls["S"] = True

        for y in range(self.height):
            # العمود الأيسر
            if (0, y) != self.entry:
                self.grid[y][0].walls["W"] = True
            # العمود الأيمن
            if (self.width - 1, y) != self.exit:
                self.grid[y][self.width - 1].walls["E"] = True

    