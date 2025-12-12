
def is_valid(a, i, j):
  n = len(a)
  m = len(a[0])
  return 0 <= i < n and 0 <= j < m

def has_access(a, i, j, l):
  di = [-1, -1, -1, 0, 1, 1, 1, 0]
  dj = [-1, 0, 1, 1, 1, 0, -1, -1]

  k = 0
  for d in range(8):
    ni, nj = i + di[d], j + dj[d]
    if is_valid(a, ni, nj) and (a[ni][nj] == "@" or a[ni][nj] == str(l)):
      k += 1

  if k < 4:
    a[i][j] = str(l)
    return True
  return False


def solve(a):
  n = len(a)
  m = len(a[0])
  sol = 0
  l = 1
  finished = False
  while not finished:
    found = False
    for i in range(n):
      for j in range(m):
        if a[i][j] == "@" and has_access(a, i, j, l):
          found = True
          sol += 1

    l += 1
    if not found:
      finished = True

  print(sol)


def main():
  with open("input.txt", "r") as f:
    a = [list(line.strip()) for line in f.readlines()]
  solve(a)

if __name__ == "__main__":
  main()

"""
..11.1121.
1@@.2.2.@2
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.

"""
