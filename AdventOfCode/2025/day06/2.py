# god help me for this ugly ass solution
# it it works it works

def solve(a, n, m):
  sum = 0
  val = 0
  op = a[n-1][0]
  for j in range(m):
    t = 10
    x = 0
    for i in range(n-1):
      if a[i][j] > 0:
        x = x * t + a[i][j]

    if a[n-1][j] != 0:
      sum += val
      val = x
      op = a[n-1][j]
    else:
      if x != 0:
        if op == -1:
          val = val + x
        else:
          val = val * x

  sum += val
  print(sum)


def main():
  with open("input.txt", "r") as f:
    lines = [line for line in f.readlines()]

  m = 3763
  n = 5
  a = [[0 for _ in range(m)] for _ in range(n)]
  for i in range(n):
    for j in range(m):
      if i in range(len(lines)) and j in range(len(lines[i])):
        if lines[i][j].isdigit():
          a[i][j] = int(lines[i][j])
        elif lines[i][j] in "+*":
          a[i][j] = -1 if lines[i][j] == "+" else -2
        else:
          a[i][j] = 0

  for i in range(n):
    for j in range(m):
      print(a[i][j], end="")
    print()

  solve(a, n, m)


if __name__ == "__main__":
  main()
