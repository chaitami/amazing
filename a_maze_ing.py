from mazegen.generator import Generator
from utils.file_management import FileManagement
from parsing import parsing
import sys
import random
import os


def path_to_coordinates(start: tuple[int,int], directions: list[str]) -> list[tuple[int,int]]:
    x, y = start
    coords = [(x, y)]
    moves = {'N': (0, -1), 'S': (0, 1), 'E': (1, 0), 'W': (-1, 0)}

    for d in directions:
        dx, dy = moves[d]
        x += dx
        y += dy
        coords.append((x, y))
    return coords


if len(sys.argv) != 2:
    print("Usage: python a_maze_ing.py config.txt")
    sys.exit(1)


config_path = sys.argv[1]
if config_path != "config.txt":
    print("Error: Config file should be named config.txt")
    sys.exit(1)
parser = parsing()
try:
    config = parser.parse_config(config_path)
    width = config.get("WIDTH")
    height = config.get("HEIGHT")
    entry = config.get("ENTRY")
    exit = config.get("EXIT")
    file = config.get("OUTPUT_FILE")
    seed = config.get("SEED")
    perfect = config.get("PERFECT", False)
except Exception as error:
    print(f"Error: {error}")

####################
# width = config.get("WIDTH")
# height = config.get("HEIGHT")
# entry = config.get("ENTRY")
# exit = config.get("EXIT")
# file = config.get("OUTPUT_FILE")
# seed = config.get("SEED")
# perfect = config.get("PERFECT", False)
####################



list_of_colors = [
    "\033[0m",   # Reset / Default
    "\033[31m",  # Red
    "\033[32m",  # Green
    "\033[33m",  # Yellow
    "\033[34m",  # Blue
    "\033[35m",  # Magenta
    "\033[36m",  # Cyan
    "\033[37m",  # White
    "\033[90m",  # Bright Black / Gray
    "\033[91m",  # Bright Red
    "\033[92m",  # Bright Green
    "\033[93m"  # Bright Yellow
]



def main():

    show = False
    color = "\033[36m"

    gen = Generator(height, width, entry, exit, seed, perfect)
    gen.generate_a_maze()
    f_obj = FileManagement(gen.get_grid())
    f_obj.write_result_to_file(file, entry, exit)
    path = f_obj.find_shortest_path(entry, exit)
    c = path_to_coordinates(entry, path)
    gen.print_maze(show, path_coords=c)
    num: int = 0
    

    while 1:
        print("\n=== A-Maze-ing ===")
        print("1. Re-generate a new maze")
        print("2. Show/Hide path from entry to exit")
        print("3. Rotate maze colors")
        print("4. Quit")
        num = int(input("Choice? (1-4): "))

        if num == 1:
            os.system("clear")
            gen = Generator(height, width, entry, exit, seed, perfect)
            gen.generate_a_maze()
            f_obj = FileManagement(gen.get_grid())
            f_obj.write_result_to_file(file, entry, exit)
            path = f_obj.find_shortest_path(entry, exit)
            c = path_to_coordinates(entry, path)
            gen.print_maze(show, path_coords=c, color=color)
            continue
        if num == 2:
            if show:
                show = False
            else:
                show = True
            os.system("clear")
            gen.print_maze(show, path_coords=c, color=color)
        if num == 3:
            color: str = random.choice(list_of_colors)
            os.system("clear")
            gen.print_maze(show, path_coords=c, color=color)
        if num == 4:
            os.system("clear")
            break
        if num < 1 or num > 4:
            break


if __name__ == "__main__":
    main()
    os.system("clear")
