from mazegen.cell_class import Cell




class FileManagement:
    def __init__(self, grid) -> None:
        self.grid = grid


    def convert_cell_to_hexa(self, cell: Cell) -> str:
        res: int = 0
        if (cell.walls['N']):
            res |= 1
        if (cell.walls['E']):
            res |= 2
        if (cell.walls['S']):
            res |= 4
        if (cell.walls['W']):
            res |= 8
        return format(res, 'X')


    def write_result_to_file(self, filename, entry, exit):
        file = open(filename, 'w')
        res = ""

        width: int = len(self.grid[0])
        height: int = len(self.grid)

        for y in range(height):
            for x in range(width):
                res += self.convert_cell_to_hexa(self.grid[y][x])
            file.write(res)
            file.write("\n")
            res = ""
        
        file.write("\n%d,%d" % (entry[0], entry[1]))
        file.write("\n%d,%d" % (exit[0], exit[1]))
        
        file.close()
 
    # def find_shortest_path(grid, start, end):
    #     width = len(grid[0])
    #     height = len(grid)
    #     dirs = {'N': (0, -1), 'E': (1, 0), 'S': (0, 1), 'W': (-1, 0)}
    #     queue = deque()
    #     queue.append((start, []))
    #     visited = set()
    #     visited.add(start)

    #     while queue:
    #         (x, y), path = queue.popleft()
    #         if (x, y) == end:
    #             return path
    #         cell = grid[y][x]
    #         for d, (dx, dy) in dirs.items():
    #             nx, ny = x + dx, y + dy
    #             if 0 <= nx < width and 0 <= ny < height and (nx, ny) not in visited:
    #                 if not cell.walls[d]:
    #                     queue.append(((nx, ny), path + [d]))
    #                     visited.add((nx, ny))
    #     return []

