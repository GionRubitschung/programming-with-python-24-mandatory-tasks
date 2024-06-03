from enum import Enum
from math import gcd
from pathlib import Path

from matrix import Matrix2Dim

from collections import deque
from typing import List, Tuple


class Sub(Enum):
    ALIEN = 0
    SHIP = 1


def common_divisor(a: int | Sub, b: int | Sub) -> bool:
    """
    Check if two numbers have a common divisor greater than 1.

    Args:
      a (int | Sub): The first number.
      b (int | Sub): The second number.

    Returns:
      bool: True if the two numbers have a common divisor greater than 1, False otherwise.
    """
    a = 1 if isinstance(a, Sub) else a
    b = 1 if isinstance(b, Sub) else b
    return gcd(a, b) > 1


def get_neighbors(maze: Matrix2Dim, cell: Tuple[int, int]) -> List[Tuple[int, int]]:
    """
    Returns a list of neighboring cells for a given cell in a maze.

    Args:
      maze (Matrix2Dim): The maze represented as a 2-dimensional matrix.
      cell (Tuple[int, int]): The coordinates of the cell for which to find neighbors.

    Returns:
      List[Tuple[int, int]]: A list of neighboring cells.
    """
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    neighbors = []
    for dx, dy in directions:
        nx, ny = cell[0] + dx, cell[1] + dy
        if (
            0 <= nx < maze.dimensions[0]
            and 0 <= ny < maze.dimensions[1]
            and (
                common_divisor(maze[cell], maze[nx, ny])
                or isinstance(maze[cell], Sub)
                or isinstance(maze[nx, ny], Sub)
            )
        ):
            neighbors.append((nx, ny))
    return neighbors


def find_path(
    maze: Matrix2Dim, start: Tuple[int, int], end: Tuple[int, int]
) -> List[int]:
    """
    Finds a path from the start cell to the end cell in a given maze.

    Args:
      maze (Matrix2Dim): The maze represented as a 2-dimensional matrix.
      start (Tuple[int, int]): The coordinates of the start cell.
      end (Tuple[int, int]): The coordinates of the end cell.

    Returns:
      List[int]: The path from the start cell to the end cell as a list of integers.
    """
    visited = {start}
    queue = deque([(start, [maze[start]])])
    while queue:
        cell, path = queue.popleft()
        if cell == end:
            return path
        for neighbor in get_neighbors(maze, cell):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [maze[neighbor]]))
    return []


def find_start_end(maze: Matrix2Dim) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    """
    Finds the start and end positions in the given maze.

    Args:
      maze (Matrix2Dim): The maze represented as a 2-dimensional matrix.

    Returns:
      Tuple[Tuple[int, int], Tuple[int, int]]: A tuple containing the start and end positions in the maze.
    """
    start, end = None, None
    for i in range(maze.dimensions[0]):
        for j in range(maze.dimensions[1]):
            if isinstance(maze[i, j], Sub):
                if maze[i, j] == Sub.ALIEN:
                    start = (i, j)
                elif maze[i, j] == Sub.SHIP:
                    end = (i, j)
    return start, end


def load_maze(file_path: Path) -> Matrix2Dim:
    """
    Load a maze from a file and return it as a 2-dimensional matrix.

    Args:
      file_path (Path): The path to the file containing the maze.

    Returns:
      Matrix2Dim: A 2-dimensional matrix representing the maze, where each element
            can be either an integer, "X" (representing a ship), "Y" (representing an alien),
            or a string.
    """
    with open(file_path, "r") as file:
        elements = [
            [
                (
                    int(num)
                    if num.isdigit()
                    else Sub.ALIEN if num == "Y" else Sub.SHIP if num == "X" else num
                )
                for num in line.split()
            ]
            for line in file
        ]
    return Matrix2Dim((len(elements), len(elements[0])), elements)


def main():
    file_path = Path("alien.txt")
    maze = load_maze(file_path)
    start, end = find_start_end(maze)

    if start is None or end is None:
        print("No alien and spaceship found in the maze.")
        return

    path = find_path(maze, start, end)
    if path:
        print(" -> ".join(map(str, path)))
    else:
        print("No path found from the alien to the spaceship.")


if __name__ == "__main__":
    main()
