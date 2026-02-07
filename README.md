*This project has been created as part of the 42 curriculum by yoech-ch, hel-achh.*

# A-Maze-ing 🌀

## Description

**A-Maze-ing** is a command-line maze generator and solver written in Python. The program reads a configuration file to define maze dimensions, entry/exit points, and an optional seed for reproducibility. It then generates a perfect maze (a maze with exactly one path between any two points) using a randomized depth-first search algorithm, displays it in the terminal, solves it by finding the shortest path, and exports the result to a file.

### Key Features

- Configurable maze dimensions, entry, exit, and seed via a simple config file
- Maze generation using **Randomized Depth-First Search** (recursive backtracker)
- Shortest path solving using **BFS (Breadth-First Search)**
- Terminal display of both the unsolved and solved maze
- Export maze to an output file
- Interactive menu for choosing actions

---

## Instructions

### Prerequisites

- **Python 3.10+** installed on your system
- `pip` package manager

### Installation

```bash
git clone <repository-url> amazing
cd amazing
make install
```

This installs all dependencies listed in `requirements.txt` (flake8, mypy, pytest).

### Execution

```bash
make run
```

Or manually:

```bash
python3 a_maze_ing.py config.txt
```

### Debug Mode

```bash
make debug
```

Launches the program with Python's built-in debugger (`pdb`).

### Linting

```bash
make lint          # mandatory checks (flake8 + mypy with required flags)
make lint-strict   # optional strict mypy checks
```

### Clean

```bash
make clean
```

Removes `__pycache__`, `.mypy_cache`, `.pytest_cache`, and compiled `.pyc`/`.pyo` files.

---

## Config File Structure

The configuration is defined in a plain-text file named `config.txt` at the project root. Each parameter is on its own line in `KEY=VALUE` format.

| Key           | Required | Type       | Range / Constraints                        | Description                        |
|---------------|----------|------------|--------------------------------------------|------------------------------------|
| `WIDTH`       | ✅       | Integer    | `1 – 100`                                  | Width of the maze (in cells)       |
| `HEIGHT`      | ✅       | Integer    | `1 – 100`                                  | Height of the maze (in cells)      |
| `ENTRY`       | ✅       | `x,y`     | Must be on the maze border                 | Entry point coordinates            |
| `EXIT`        | ✅       | `x,y`     | Must be on the maze border                 | Exit point coordinates             |
| `SEED`        | ❌       | Integer    | Any integer (omit for random generation)   | Seed for reproducible mazes        |
| `OUTPUT_FILE` | ❌       | String     | Default: `maze.txt` (saved in `output/`)   | Name of the output file            |

### Example `config.txt`

```txt
WIDTH=20
HEIGHT=10
ENTRY=0,0
EXIT=19,9
SEED=42
OUTPUT_FILE=maze.txt
```

### Notes

- Lines starting with `#` are treated as comments (recommended but not guaranteed in current version).
- `ENTRY` and `EXIT` must be on the border of the maze grid.
- `ENTRY` and `EXIT` must not be the same point.
- If `SEED` is omitted, the maze is generated randomly each run.

---

## Maze Generation Algorithm

### Algorithm: Randomized Depth-First Search (Recursive Backtracker)

The maze is generated using the **Randomized DFS / Recursive Backtracker** algorithm.

#### How It Works

1. Start with a grid where every cell is surrounded by walls.
2. Choose a starting cell (the entry point) and mark it as visited.
3. From the current cell, pick a random unvisited neighbor.
4. Remove the wall between the current cell and the chosen neighbor.
5. Move to the chosen neighbor and repeat from step 3.
6. If the current cell has no unvisited neighbors, backtrack to the previous cell.
7. Repeat until all cells have been visited.

#### Result

This produces a **perfect maze** — one with:
- Exactly **one path** between any two cells
- **No loops** and **no isolated sections**

### Why This Algorithm?

| Reason                    | Details                                                                 |
|---------------------------|-------------------------------------------------------------------------|
| **Simplicity**            | Easy to understand and implement with a stack or recursion              |
| **Perfect mazes**         | Guarantees a unique solution between any two points                     |
| **Long, winding paths**   | Produces aesthetically pleasing mazes with long corridors               |
| **Seed support**          | Combined with `random.seed()`, mazes are fully reproducible             |
| **Educational value**     | Excellent for learning graph traversal and backtracking                 |

Alternative algorithms considered:
- **Kruskal's** — produces shorter, more branching paths; more complex to implement.
- **Prim's** — similar output but less intuitive for grid-based mazes.
- **Eller's** — row-by-row generation, harder to debug and visualize.

---

## Reusable Code

The project is structured in modular packages that can be reused independently:

| Module / Package         | Reusable For                                                        |
|--------------------------|---------------------------------------------------------------------|
| `mazegen/generator.py`   | Any project needing procedural maze generation on a 2D grid         |
| `utils/file_management.py` | BFS shortest-path solver — reusable for any grid-based pathfinding |
| `parsing.py`             | Generic `KEY=VALUE` config file parser                              |
| `display.py`             | Terminal-based 2D grid rendering                                    |

### How to Reuse

```python
from mazegen.generator import Generator

gen = Generator(width=20, height=10, entry=(0, 0), exit_=(19, 9), seed=42)
maze = gen.generate_a_maze()
```

The `Generator` class is self-contained and only depends on the Python standard library (`random`). It can be imported into any Python project without modification.

---

## Team & Project Management

### Team Members & Roles

| Member       | Role                                                                 |
|--------------|----------------------------------------------------------------------|
| **yoech-ch** | Display rendering, config parsing, Makefile, README & documentation |
| **hel-achh** | Maze generation (DFS), solver (BFS), file export, project architecture |

### Planning & Timeline

| Phase              | Planned         | Actual          | Notes                                      |
|--------------------|-----------------|-----------------|---------------------------------------------|
| Research           | Day 1           | Day 1           | Algorithm comparison and selection          |
| Architecture       | Day 1–2         | Day 1–2         | Module structure, config parsing            |
| Maze generation    | Day 2–3         | Day 2–3         | Recursive DFS implementation                |
| Solver (BFS)       | Day 3           | Day 3–4         | Took longer due to wall encoding            |
| Display & export   | Day 4           | Day 4           | Terminal rendering and file output          |
| Testing & fixes    | Day 5           | Day 5–6         | Edge cases, config validation               |
| Documentation      | Day 6           | Day 6           | README, Makefile, comments                  |

### What Worked Well

- Modular architecture made debugging and testing straightforward
- Using a seed for reproducibility greatly simplified testing
- The recursive backtracker was a good fit for the project scope

### What Could Be Improved

- Input validation could be more robust (bounds checking, border validation)
- Recursive DFS hits Python's recursion limit on very large mazes (100×100)
- The interactive menu could handle invalid input more gracefully

### Tools Used

| Tool          | Purpose                              |
|---------------|--------------------------------------|
| Python 3      | Main programming language            |
| Git           | Version control                      |
| VS Code       | IDE                                  |
| flake8        | Code style linting                   |
| mypy          | Static type checking                 |
| pytest        | Unit testing                         |
| Make          | Build automation                     |

---

## Resources

### Documentation & References

- [Maze Generation Algorithm — Wikipedia](https://en.wikipedia.org/wiki/Maze_generation_algorithm)
- [Recursive Backtracker — Think Labyrinth](http://www.astrolog.org/labyrnth/algrithm.htm)
- [BFS Shortest Path — GeeksforGeeks](https://www.geeksforgeeks.org/shortest-path-unweighted-graph/)
- [Python `random` module documentation](https://docs.python.org/3/library/random.html)
- [Makefile Tutorial](https://makefiletutorial.com/)

### AI Usage

| Task                        | AI Used | Details                                                       |
|-----------------------------|---------|---------------------------------------------------------------|
| Makefile creation           | ✅      | GitHub Copilot assisted with Makefile structure and rules     |
| Bug analysis                | ✅      | GitHub Copilot used to systematically trace code paths and identify edge-case crashes |
| README writing              | ✅      | GitHub Copilot assisted with structuring and formatting       |
| Core algorithm (DFS/BFS)    | ❌      | Implemented manually based on Wikipedia pseudocode            |
| Config parsing              | ❌      | Written manually                                              |
| Display rendering           | ❌      | Written manually                                              |

> AI was used as a **productivity tool** for documentation, review, and testing — not for writing the core maze generation or solving logic.