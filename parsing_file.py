import sys

class parsing:
    def __init__(self):
        pass

    def parse_config(self, filename):
        try:
            data = {}
            with open(filename) as file:
                for line in file:
                    line = line.strip()
                    if not line or line.startswith("#"):
                        continue
                    if line.find("=") == -1:
                        raise ValueError("Invalid line in config:"
                                         f"{line}")
                    key = line.split("=")[0].strip()
                    value = line.split("=")[1].strip()

                    if key in data:
                        raise ValueError(f"Duplicate key '{key}'")

                    if key == "WIDTH":
                        try:
                            value = int(value)
                        except ValueError:
                            raise ValueError("WIDTH should be an integer")

                        if value <= 0:
                            raise ValueError("WIDTH should be a positive integer")
                        elif value > 100:
                            raise ValueError("WIDTH should be less than or equal to 100")
                        data[key] = value

                    elif key == "HEIGHT":
                        try:
                            value = int(value)
                        except ValueError:
                            raise ValueError("HEIGHT should be an integer")

                        if value <= 0:
                            raise ValueError("HEIGHT should be a positive integer")
                        elif value > 100:
                            raise ValueError("HEIGHT should be less than or equal to 100")
                        data[key] = int(value)

                    elif key == "ENTRY":
                        ex, ey = value.split(",")
                        try:
                            ex = int(ex)
                            ey = int(ey)
                        except ValueError:
                            raise ValueError("ENTRY should be in the format x,y where x and y are integers")
                        if ex < 0 or ey < 0:
                            raise ValueError("ENTRY coordinates should be non-negative integers")
                        elif int(ex) > 100 or int(ey) > 100:
                            raise ValueError("ENTRY coordinates should be less than or equal to 100")
                        data[key] = (ex, ey)

                    elif key == "EXIT":
                        xx, xy = value.split(",")
                        try:
                            xx = int(xx)
                            xy = int(xy)
                        except ValueError:
                            raise ValueError("EXIT should be in the format x,y where x and y are integers")
                        if xx < 0 or xy < 0:
                            raise ValueError("EXIT coordinates should be non-negative integers")
                        elif int(xx) > 100 or int(xy) > 100:
                            raise ValueError("EXIT coordinates should be less than or equal to 100")
                        data[key] = (xx, xy)

                    elif key == "PERFECT":
                        perfect = parsing.parse_bool(value)
                        if perfect is None:
                            raise ValueError("PERFECT should be a boolean")
                        data[key] = perfect
                    # Modification here : ........
                    elif key == "OUTPUT_FILE":
                        if value == "":
                            raise ValueError("OUTPUT_FILE shouldn't be Empty")
                        else:
                            data[key] = value

                    elif key == "SEED":
                        v = value.strip().lower()
                        if v in ("none", ""):
                            data[key] = None
                        else:
                            try:
                                data[key] = int(v)
                            except ValueError:
                                raise ValueError("SEED must be an integer or None")

            return data
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)

    @staticmethod
    def parse_bool(value: str) -> bool:
        v = value.strip().lower()
        if v in {"true", "1", "yes", "y"}:
            return True
        if v in {"false", "0", "no", "n"}:
            return False
