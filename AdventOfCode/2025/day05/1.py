
def solve(ranges, ingredients):
  k = 0
  for ingredient in ingredients:
    for r in ranges:
      if r[0] <= ingredient <= r[1]:
        k += 1
        break

  return k


def main():
  with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

  ranges = []
  ingredients = []

  for line in lines:
    if line.find("-") != -1:
      parts = line.split("-")
      ranges.append((int(parts[0]), int(parts[1])))
    elif line != "":
      ingredients.append(int(line))

  print(solve(ranges, ingredients))


if __name__ == "__main__":
  main()
