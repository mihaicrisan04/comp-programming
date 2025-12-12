
def main():
  with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

  a = [line.split() for line in lines]
  n = len(a)
  m = len(a[0])

  sum = 0
  for j in range(m):
    op = a[n-1][j]
    if op == "*":
      x = 1
    elif op == "+":
      x = 0
    else:
      x = 0 # not possible via the problem requirements

    for i in range(n-1):
      if op == "*":
        x *= int(a[i][j])
      elif op == "+":
        x += int(a[i][j])

    sum += x

  print(sum)

if __name__ == "__main__":
  main()
