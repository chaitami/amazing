from utils.file_management import FileManagement
from utils.helper_functions import path_to_coordinates, print_maze
from parsing.parsing_file import parsing
from mazegen import MazeGenerator
import random
import sys
import os



list_of_colors = [
    "\033[0m",
    "\033[31m",
    "\033[32m",
    "\033[33m",
    "\033[34m",
    "\033[35m",
    "\033[36m",
    "\033[37m",
    "\033[90m",
    "\033[91m",
    "\033[92m",
    "\033[93m"
]


def main():

    if len(sys.argv) != 2:
        print("Usage: python a_maze_ing.py config.txt")
        sys.exit(1)
    # Modification here : ........
    config_path = sys.argv[1]
    parser = parsing()
    try:
        config = parser.parse_config(config_path)
        width = config["WIDTH"]
        height = config["HEIGHT"]
        entry = config["ENTRY"]
        exit = config["EXIT"]
        file = config["OUTPUT_FILE"]
        perfect = config["PERFECT"]
        seed = config["SEED"]
        ex, ey = entry
        xx, xy = exit

        if ex >= width or ey >= height:
            raise ValueError("ENTRY outside maze bounds")

        if xx >= width or xy >= height:
            raise ValueError("EXIT outside maze bounds")

        if entry == exit:
            raise ValueError("ENTRY and EXIT must be different")

        if width is None or height is None or entry is None or exit is None or file is None or perfect is None:
            raise Exception("Missing required configuration parameters.")
    except Exception as error:
        print(f"Error: {error}")
        sys.exit(1)    



    os.system("clear")
    print("\033[H\033[2J\033[3J", end="")
    show = False
    color = "\033[36m"

    try:
        gen = MazeGenerator(height, width, entry, exit, seed, perfect)
        gen.generate_a_maze(use_pattern=True)

        f_obj = FileManagement(gen.get_grid())

        f_obj.write_result_to_file(file, entry, exit)

        path = gen.find_shortest_path()

        c = path_to_coordinates(entry, path)
        print_maze(show, path_coords=c, grid=gen.get_grid(), entry=entry, exit=exit)

    except Exception as o:
        print(o)
        return

    
    try:
        num: int = 0 
        while 1:
            print("\n=== A-Maze-ing ===")
            print("1. Re-generate a new maze")
            print("2. Show/Hide path from entry to exit")
            print("3. Rotate maze colors")
            print("4. Quit")
            try:
                num = int(input("Choice? (1-4): "))
            except KeyboardInterrupt:
                return

            if num == 1:
                os.system("clear")
                print("\033[H\033[2J\033[3J", end="")
                gen = MazeGenerator(height, width, entry, exit, seed, perfect)
                gen.generate_a_maze(use_pattern=True)
                f_obj = FileManagement(gen.get_grid())
                f_obj.write_result_to_file(file, entry, exit)
                path = gen.find_shortest_path()
                c = path_to_coordinates(entry, path)
                print_maze(show, path_coords=c, color=color, grid=gen.get_grid(), entry=entry, exit=exit)
                continue

            if num == 2:
                if show:
                    show = False
                else:
                    show = True
                os.system("clear")
                print("\033[H\033[2J\033[3J", end="")
                print_maze(show, path_coords=c, color=color, grid=gen.get_grid(), entry=entry, exit=exit)

            if num == 3:
                color: str = random.choice(list_of_colors)
                os.system("clear")
                print("\033[H\033[2J\033[3J", end="")
                print_maze(show, path_coords=c, color=color, grid=gen.get_grid(), entry=entry, exit=exit)

            if num == 4:
                os.system("clear")
                print("\033[H\033[2J\033[3J", end="")
                break

            if num < 1 or num > 4:
                break
    except Exception as error:
        os.system("clear")
        print("\033[H\033[2J\033[3J", end="")
        print(error)
        return




if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(error)
