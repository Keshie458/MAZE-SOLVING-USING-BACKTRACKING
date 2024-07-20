import time
import tkinter as tk


def is_safe(maze, x, y, solution):
    """
    Check if maze[x][y] is a valid move.
    """
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 1 and solution[x][y] == 0


def solve_maze_util(maze, x, y, solution, path, counter):
    """
    Utilizes backtracking to find a solution to the maze.
    """
    counter[0] += 1
    if x == len(maze) - 1 and y == len(maze[0]) - 1:
        solution[x][y] = 1
        path.append((x, y))
        return True

    if is_safe(maze, x, y, solution):
        solution[x][y] = 1
        path.append((x, y))

        # Move down
        if solve_maze_util(maze, x + 1, y, solution, path, counter):
            return True

        # Move right
        if solve_maze_util(maze, x, y + 1, solution, path, counter):
            return True

        # Move up
        if solve_maze_util(maze, x - 1, y, solution, path, counter):
            return True

        # Move left
        if solve_maze_util(maze, x, y - 1, solution, path, counter):
            return True

        # Backtrack
        solution[x][y] = 0
        path.pop()
        return False

    return False


def solve_maze(maze):
    """
    Solves the maze using backtracking.
    """
    solution = [[0] * len(maze[0]) for _ in range(len(maze))]
    path = []
    counter = [0]  # To count the number of recursive calls

    start_time = time.time()
    solved = solve_maze_util(maze, 0, 0, solution, path, counter)
    end_time = time.time()

    execution_time = end_time - start_time
    complexity = counter[0]

    if not solved:
        return None, None, execution_time, complexity, 0

    path_length = len(path)
    return solution, path, execution_time, complexity, path_length


class MazeVisualizer:
    def __init__(self, maze, path):
        self.maze = maze
        self.path = path
        self.window = tk.Tk()
        self.window.title("Maze Solver Visualization")
        self.canvas = tk.Canvas(self.window, width=600, height=600)
        self.canvas.pack()
        self.cell_size = 600 // len(maze)
        self.draw_maze()
        self.animate_path()
        self.window.mainloop()

    def draw_maze(self):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[0])):
                x1 = j * self.cell_size
                y1 = i * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                if self.maze[i][j] == 1:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="white")
                else:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="black")

    def animate_path(self):
        for (x, y) in self.path:
            x1 = y * self.cell_size
            y1 = x * self.cell_size
            x2 = x1 + self.cell_size
            y2 = y1 + self.cell_size
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="green")
            self.window.update()
            self.window.after(100)  # Adjust the speed of animation here


def test_maze_solutions():
    mazes = {
        "small": [
            [1, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 1, 0, 0],
            [1, 1, 1, 1]
        ],
        "medium": [
            [1, 0, 0, 0, 1, 1, 0, 1, 1, 0],
            [1, 1, 1, 0, 1, 0, 0, 1, 0, 1],
            [0, 0, 1, 1, 1, 1, 1, 0, 1, 0],
            [1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
            [0, 1, 1, 1, 0, 1, 0, 0, 0, 1],
            [1, 0, 0, 1, 1, 1, 0, 1, 1, 1],
            [0, 1, 1, 1, 0, 1, 1, 1, 0, 0],
            [1, 0, 1, 0, 1, 1, 0, 1, 1, 1],
            [0, 1, 0, 1, 0, 1, 1, 0, 1, 1],
            [1, 1, 1, 1, 1, 0, 1, 1, 1, 1]
        ],
        "large": [
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
            [0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
            [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1],
            [0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0],
            [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1],
            [0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1],
            [1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1],
            [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1],
            [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0],
            [0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1],
            [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
            [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
            [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]
    }

    for size, maze in mazes.items():
        solution, path, execution_time, complexity, path_length = solve_maze(maze)
        if solution and path:
            print(f"{size.capitalize()} maze solved!")
            print(f"Execution time: {execution_time:.4f} seconds")
            print(f"Number of recursive calls: {complexity}")
            print(f"Path length: {path_length}")
            visualizer = MazeVisualizer(maze, path)
        else:
            print(f"{size.capitalize()} maze has no solution!")


test_maze_solutions()
