from mazegen.generator import Generator
from utils.file_management import FileManagement



# RESET = "\033[0m"
# RED   = "\033[31m"
# GREEN = "\033[32m"
# YELLOW= "\033[33m"
# BLUE  = "\033[34m"
# MAGENTA = "\033[35m"
# CYAN  = "\033[36m"
# WHITE = "\033[37m"



width = 10
height = 10
entry = 0,0
exit = 19,14
file = "test.txt"
seed=8
perfect=True



gen = Generator(height, width, entry, exit, seed, perfect)
gen.generate_a_maze()


f_obj = FileManagement(gen.get_grid())
f_obj.write_result_to_file(file, entry, exit)
gen.print_maze()

