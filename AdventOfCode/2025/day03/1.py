def get_max_joltage(line):
  l, r = 0, 1
  max_joltage = -1
  while (l < r and r < len(line)):
    joltage = int(line[l]) * 10 + int(line[r])
    if joltage > max_joltage:
      max_joltage = joltage

    if line[l] < line[r]:
      l += 1
      if l == r:
       r += 1
    else:
      r += 1

  return max_joltage


def main():
  with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

  print(sum(get_max_joltage(line) for line in lines))


if __name__ == "__main__":
  main()
