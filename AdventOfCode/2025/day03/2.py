
def get_max_joltage(line):
  res = [0 for _ in range(12)]
  n = len(line)
  k = 0
  i = 0
  while i < n:
    if k >= 12:
      break
    res[k] = line[i]
    pos = (n-1) - (11 - k)
    found = False
    for j in range(n-1 - (11-k) , i-1, -1):
      if line[j] >= res[k]:
        res[k] = line[j]
        found = True
        pos = j

    i = pos + 1 if found else i + 1
    k += 1

  joltage = int(''.join(map(str, res)))
  return joltage


def main():
  with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

  print(sum(get_max_joltage(line) for line in lines))

if __name__ == "__main__":
  main()
