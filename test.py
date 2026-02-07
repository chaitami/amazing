class cell:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.walls = {"N":True, "S": True, "E": True, "W": True}
        self.visited = False




def create_grid(width, height):
    row = []
    result = []

    for y in range(height):
        for x in range(width):
            obj = cell(x, y)
            row.append(obj)
        result.append(row)
        row = []

    return result


def print_maze(grid):
    RESET = "\033[0m"
    color = "\033[0m"
    RED   = "\033[31m"

    height = len(grid)
    width = len(grid[0])


    for y in range(height):
        top = ''
        for x in range(width):
            top += '+' + color + '━━━' if grid[y][x].walls['N'] else '   '
        print(top + '+')
        side = ''
        for x in range(width):
            side += '┃' + color if grid[y][x].walls['W'] else ' '
            side += '   '
        side += '┃' + color
        print(side)
    bottom = ''
    for x in range(width):
        bottom += '+' + (color + '━━━' if grid[height-1][x].walls['S'] else '   ')
    print(bottom + '+')


ggrid = create_grid(5, 5)


print_maze(ggrid)
