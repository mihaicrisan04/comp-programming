# aoc_2025_day1.py
from string import printable
import sys
from typing import Iterable

def parse_lines(lines: Iterable[str]) -> list[tuple[str, int]]:
    moves: list[tuple[str, int]] = []
    for raw in lines:
        s = raw.strip()
        if not s:
            continue
        # Expect format like "L68" or "R14"
        dir_char = s[0]
        if dir_char not in ("L", "R"):
            raise ValueError(f"Invalid direction in line: {s}")
        try:
            dist = int(s[1:])
        except ValueError:
            raise ValueError(f"Invalid distance in line: {s}")
        moves.append((dir_char, dist))
    return moves

def compute_password(moves: list[tuple[str, int]]) -> int:
    pos = 50  # starting position
    zeros = 0
    for dir_char, dist in moves:
        if dir_char == "L":
            pos = (pos - dist) % 100
        else:  # "R"
            pos = (pos + dist) % 100
        if pos == 0:
            zeros += 1
    return zeros

def main() -> None:
    # Read input from input file
    with open("input.txt", "r") as f:
        lines = f.readlines()
    moves = parse_lines(lines)
    result = compute_password(moves)
    print(result)

if __name__ == "__main__":
    main()
