


# def read_file():
#     file_name = 'data.in'
#     with open(file_name, 'r') as f:
#         lines = f.readlines()
#         return lines

# def main() -> None:
#     lines = read_file()
#     print(lines)

# if __name__ == '__main__':
#     main()  


# from typing import List

# file = open('data.in').read().strip().split("\n\n")

# seeds = [int(x) for x in file[0].replace("seeds: ", "").split(" ")]

# # Map format: [[destination_range_start, source_range_start, range_length], ...]
# maps = [
#     [[int(y) for y in x.split(" ")] for x in file[i].splitlines()[1::]]
#     for i in range(1, 8)
# ]


# def x_to_y(step: int, m: List[List[int]]) -> int:
#     for destination_range_start, source_range_start, range_length in m:
#         if step >= source_range_start and step < source_range_start + range_length:
#             step = destination_range_start + (step - source_range_start)
#             break

#     return step


# r = float("inf")

# for seed in seeds:
#     for m in maps:
#         seed = x_to_y(seed, m)
#     r = min(r, seed)

# print(r)

file = open('data.in').read().strip().split("\n\n")

inputs = [int(x) for x in file[0].replace("seeds: ", "").split(" ")]

# Seeds format: [(start, end), ...]
seeds = [(inputs[i], inputs[i] + inputs[i + 1]) for i in range(0, len(inputs), 2)]

# Map format: [[destination_range_start, source_range_start, range_length], ...]
maps = [
    [[int(y) for y in x.split(" ")] for x in file[i].splitlines()[1::]]
    for i in range(1, 8)
]


def remap(start: int, end: int, new_seeds: list[tuple[int]], m: list[int]) -> int:
    for destination_range_start, source_range_start, range_length in m:
        # Check if the ranges overlap
        overlap_start = max(start, source_range_start)
        overlap_end = min(end, source_range_start + range_length)

        if overlap_start < overlap_end:
            new_seeds.append(
                (
                    destination_range_start + (overlap_start - source_range_start),
                    destination_range_start + (overlap_end - source_range_start),
                )
            )

            if start < overlap_start:
                seeds.append((start, overlap_start))

            if overlap_end < end:
                seeds.append((overlap_end, end))

            break
    else:
        # If no overlap, just add the original range to the new seeds
        new_seeds.append((start, end))


r = float("inf")

for m in maps:
    new_seeds = []
    while len(seeds) > 0:
        start, end = seeds.pop()
        remap(start, end, new_seeds, m)

    seeds = new_seeds

print(min(seeds)[0])