
def solve(ranges):
  ranges.sort()
  max_end = ranges[0][1]
  total = ranges[0][1] - ranges[0][0] + 1

  for i in range(1, len(ranges)):
    start, end = ranges[i]
    if start <= max_end:
      if end > max_end:
        total += end - max_end
    else:
      total += end - start + 1

    max_end = max(max_end, end)

  return total


def main():
  with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

  ranges = []

  for line in lines:
    if line.find("-") != -1:
      parts = line.split("-")
      ranges.append((int(parts[0]), int(parts[1])))
    else:
      break

  print(solve(ranges))


if __name__ == "__main__":
  main()
