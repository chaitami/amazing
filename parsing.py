
class parsing:
    def __init__(self):
        pass

    def parse_config(self, filename):

        data = {}

        with open(filename) as file:
            for line in file:
                key = line.split("=")[0].strip()
                value = line.split("=")[1].strip()
                if key == "WIDTH":
                    data[key] = int(value)
                elif key == "HEIGHT":
                    data[key] = int(value)
                elif key == "ENTRY":
                    parts = value.split(",")
                    data[key] = (int(parts[0].strip()), int(parts[1].strip()))
                elif key == "EXIT":
                    parts = value.split(",")
                    data[key] = (int(parts[0].strip()), int(parts[1].strip()))
                elif key == "PERFECT":
                    data[key] = parsing.parse_bool(value)
                elif key == "OUTPUT_FILE":
                    data[key] = value
                elif key == "SEED":
                    if value.isdigit():
                        data[key] = int(value)
                    elif value.lower() == "none" or value == "":
                        data[key] = None

        return data

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
