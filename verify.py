
class cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = False
        self.walls = {"N": True, "S": True, "W": True, "E": True}


def creategrid(width, height):
    result = []
    row = []

    for x in range(height):
        for y in range(width):
            col = cell(x, y)
            row.append(col)
        result.append(row)
        row = []
    return result

def print_maze(grid):

    height = len(grid)
    width = len(grid[0])
    
    for x in range(height):
        top = ''
        for y in range(width):
            top += '+' + ('━━━' + if grid[x][y].walls['N'] else '   ')
        print(top + '+')
        side = ''
        for y in range(width):
            side += '┃' + if grid[x][y].walls['W'] else '   '
            side += '   '
            side += '┃' + if grid[x][y].walls['E'] else '   '
        print(side)

    bottom = ''
    for y in range(width):
        bottom += '+' + '━━━' + if grid[height-1][y].walls['S'] else '   '
    print(bottom + '+')

def print_maze(grid):
    height = len(grid)
    width = len(grid[0])

    for y in range(height):
        top = ''
        for x in range(width):
            top += '+' + ('━━━' if grid[y][x].walls['N'] else '   ')
        print(top + '+')

        side = ''
        for x in range(width):
            side += ('┃' if grid[y][x].walls['W'] else ' ')
            side += '   '
        side += '┃'
        print(side)

    bottom = ''
    for x in range(width):
        bottom += '+' + ('━━━' if grid[height-1][x].walls['S'] else '   ')
    print(bottom + '+')


test = creategrid(5,5)
print_maze(test)
    

         