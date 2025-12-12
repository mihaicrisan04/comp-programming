
def is_valid(a, i, j):
  n = len(a)
  m = len(a[0])
  return 0 <= i < n and 0 <= j < m

def has_access(a, i, j):
  di = [-1, -1, -1, 0, 1, 1, 1, 0]
  dj = [-1, 0, 1, 1, 1, 0, -1, -1]

  k = 0
  for d in range(8):
    ni, nj = i + di[d], j + dj[d]
    if is_valid(a, ni, nj) and a[ni][nj] == "@":
      k += 1

  return True if k < 4 else False


def solve(a):
  n = len(a)
  m = len(a[0])

  sol = 0
  for i in range(n):
    for j in range(m):
      if a[i][j] == "@" and has_access(a, i, j):
        sol += 1

  print(sol)


def main():
  with open("input.txt", "r") as f:
    a = [line.strip() for line in f.readlines()]
  solve(a)

if __name__ == "__main__":
  main()
