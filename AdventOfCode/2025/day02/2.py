from operator import sub
import sys

def count_substring(text, substring):
  count = 0
  start = 0
  while True:
    pos = text.find(substring, start)
    if pos == -1:
      break
    count += 1
    start = pos + len(substring)

  return count

def solve(ranges):
  sum = 0

  for r in ranges:
    start, end = r[0], r[1]

    for i in range(start, end + 1):
      i = str(i)
      for j in range(1, len(i)):
        substring = i[0:j]
        substring_length = len(substring)
        count = count_substring(i, substring)
        if count >= 2 and substring_length * count == len(i):

          sum += int(i)
          # print(i, substring, count)
          break

  return sum


def main() -> None:
  with open("input.txt", "r") as f:
    lines = f.readlines()
  ranges = lines[0].strip().split(",")
  ranges = [tuple(map(int, r.split("-"))) for r in ranges]

  sum = solve(ranges)
  print(sum)

if __name__ == "__main__":
  main()
