# aoc_2025_day1_part2_file.py
import sys
from typing import List, Tuple

def parse_lines(lines: List[str]) -> List[Tuple[str, int]]:
    moves: List[Tuple[str, int]] = []
    for raw in lines:
        s = raw.strip()
        if not s:
            continue
        dir_char = s[0]
        if dir_char not in ("L", "R"):
            raise ValueError(f"Invalid direction in line: {s}")
        try:
            dist = int(s[1:])
        except ValueError:
            raise ValueError(f"Invalid distance in line: {s}")
        moves.append((dir_char, dist))
    return moves

def count_zero_hits_during(p: int, dir_char: str, d: int) -> int:
    """
    Count 0 hits during the rotation (not including the final click if it lands on 0).
    - Right: every time p + k crosses 100, we hit 0. Count floor((p + d) / 100).
    - Left: we hit 0 after p left-clicks, then each additional 100 clicks:
      0 if d < p; else 1 + floor((d - p) / 100).
    """
    if d <= 0:
        return 0
    if dir_char == "R":
        return (p + d) // 100
    else:
        if d < p:
            return 0
        return 1 + (d - p) // 100

def compute_password_method_click(moves: List[Tuple[str, int]]) -> int:
    """
    Method 0x434C49434B: count every time the dial points at 0 during any click,
    including when a rotation ends at 0.
    """
    pos = 50
    zeros = 0
    for dir_char, dist in moves:
        zeros += count_zero_hits_during(pos, dir_char, dist)
        if dir_char == "R":
            pos = (pos + dist) % 100
        else:
            pos = (pos - dist) % 100
        if pos == 0:
            zeros += 1
    return zeros

def main() -> None:
    try:
        with open("input.txt", "r", encoding="utf-8") as f:
            lines = f.read().splitlines()
    except FileNotFoundError:
        print("Error: input.txt not found. Place your puzzle input in a file named input.txt next to this script.", file=sys.stderr)
        sys.exit(1)

    moves = parse_lines(lines)
    result = compute_password_method_click(moves)
    print(result)

if __name__ == "__main__":
    main()
