from typing import Dict


class Cell:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y
        self.visite: bool = False
        self.walls: Dict[str, bool] = {"W": True, "N": True, "E": True, "S": True}
