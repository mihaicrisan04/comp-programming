import sys


def solve(ranges):
  sum = 0

  for r in ranges:
    start, end = r[0], r[1]

    for i in range(start, end + 1):
      n = len(str(i))
      if n % 2 == 0:
        mod = n // 2
        a = i % pow(10, mod)
        b = i // pow(10, mod)
        if a == b:
          print(a, b)
          sum += i

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
