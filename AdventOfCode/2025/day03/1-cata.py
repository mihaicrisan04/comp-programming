import sys

def largest_batteries(banks):
  sum = 0
  for bank in banks:
    first = 0
    first_pos = 0
    second = 0
    second_pos = 0
    bank = bank.strip()
    n = len(bank)
    for i in range(0,n):
      aux = int(bank[i])
      if aux > first:
        first = aux
        first_pos = i
    for i in range(0,n):
      aux = int(bank[i])
      if aux > second

    print(first)
    print(first_pos)

  return sum

def main() -> None:
  with open("input.txt", "r") as f:
    lines = f.readlines()
  banks = lines
  sum = largest_batteries(banks)
  print(sum)



if __name__ == "__main__":
  main()
