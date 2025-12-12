
def inside(i, j, n, m):
  return 0 <= i < n and 0 <= j < m

def parse(a, i, j, n, m):
  if not inside(i, j, n, m):
    return 0

  a[i][j] = '|'
  if inside(i+1, j, n, m) and a[i+1][j] == '.':
    return parse(a, i+1, j, n, m)
  elif inside(i+1, j, n, m) and a[i+1][j] == '^':
    return 1 + parse(a, i+1, j-1, n, m) + parse(a, i+1, j+1, n, m)

  return 0


def solve(a):
  asn = 0
  for j in range(len(a[0])):
    if a[0][j] == 'S':
      ans = parse(a, 0, j, len(a), len(a[0]))

  for i in range(len(a)):
    print(''.join(a[i]))

  return ans

def main():
  with open("input.txt", "r") as f:
    a = [[c for c in line.strip()] for line in f.readlines()]

  print(solve(a))

if __name__ == "__main__":
  main()
