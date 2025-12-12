def inside(i, j, n, m):
  return 0 <= i < n and 0 <= j < m


def solve(a):
  n = len(a)
  m = len(a[0])

  for j in range(m):
    if a[0][j] == -2:
      a[0][j] = 1

  for i in range(n - 1):
    for j in range(m):
      if a[i][j] > 0:
        if inside(i+1, j, n, m):
          if a[i+1][j] >= 0:
            a[i+1][j] += a[i][j]
          elif a[i+1][j] == -1:
            if inside(i+1, j-1, n, m) and a[i+1][j-1] >= 0:
              a[i+1][j-1] += a[i][j]
            if inside(i+1, j+1, n, m) and a[i+1][j+1] >= 0:
              a[i+1][j+1] += a[i][j]

  ans = sum(x for x in a[n-1] if x > 0)
  return ans


def main():
  with open("input.txt", "r") as f:
    a = [[0 if c == '.' else -1 if c == '^' else -2 for c in line.strip()] for line in f.readlines()]

  print(solve(a))


if __name__ == "__main__":
  main()
