
class parsing:
    def __init__(self):
        pass

    def parse_config(self, filename):
        try:
            data = {}
            with open(filename) as file:
                for line in file:
                    if line.find("=") == -1:
                        raise ValueError("Invalid line in config:"
                                         f"{line.strip()}")
                    key = line.split("=")[0].strip()
                    value = line.split("=")[1].strip()
                    if key == "WIDTH":
                        if not value.isdigit():
                            raise ValueError("WIDTH should be an integer")
                        data[key] = int(value)
                    elif key == "HEIGHT":
                        if not value.isdigit():
                            raise ValueError("HEIGHT should be an integer")
                        data[key] = int(value)
                    elif key == "ENTRY":
                        parts = value.split(",")
                        data[key] = (int(parts[0].strip()),
                                     int(parts[1].strip()))
                    elif key == "EXIT":
                        parts = value.split(",")
                        data[key] = (int(parts[0].strip()),
                                     int(parts[1].strip()))
                    elif key == "PERFECT":
                        perfect = parsing.parse_bool(value)
                        if perfect is None:
                            raise ValueError("PERFECT should be a boolean")
                        data[key] = perfect
                    elif key == "OUTPUT_FILE":
                        if value == "maze.txt" or value == "":
                            data[key] = "maze.txt"
                        else:
                            raise ValueError("OUTPUT_FILE should be maze.txt")
                    elif key == "SEED":
                        if value.isdigit():
                            data[key] = int(value)
                        elif value.lower() == "none" or value == "":
                            data[key] = None
            return data
        except Exception as e:
            print(f"Error: {e}")

    @staticmethod
    def parse_bool(value: str) -> bool:
        v = value.strip().lower()
        if v in {"true", "1", "yes", "y"}:
            return True
        if v in {"false", "0", "no", "n"}:
            return False


if __name__ == "__main__":
    parser = parsing()
    data = parser.parse_config("config.txt")
    print(data)
