from collections import deque

# Pace to space and time mappings
pace_space = {1:1, 2:1, 3:1, 4:1, 5:1, 0:0, -1:-1, -2:-1, -3:-1, -4:-1, -5:-1}
pace_time = {1:1, 2:2, 3:3, 4:4, 5:5, 0:1, -1:1, -2:2, -3:3, -4:4, -5:5}

# Valid transitions between paces
transitions = {
    -5: [-4, 0],
    -4: [-5, -3],
    -3: [-4, -2],
    -2: [-3, -1],
    -1: [-2, 0],
    0: [-5, 5],
    5: [4, 0],
    4: [5, 3],
    3: [4, 2],
    2: [3, 1],
    1: [2, 0]
}

def find_sequence(p, t):
    """
    Find a valid pace sequence using BFS.
    Returns sequence WITHOUT the initial 0 (starts with first move).
    """
    # State: (current_pace, space_accumulated, time_used, path)
    # Start at pace 0, time=1 (standing still at start)
    queue = deque([(0, 0, 1, [])])
    visited = set()

    while queue:
        pace, space, time, path = queue.popleft()

        # Check if we reached the goal - must be at pace 0 and exact position
        if pace == 0 and space == p and len(path) > 0:
            if time <= t:
                return path
            continue

        # Prune if time exceeded
        if time > t:
            continue

        # State for visited tracking
        state = (pace, space, time)
        if state in visited:
            continue
        visited.add(state)

        # Try all possible transitions
        for next_pace in transitions[pace]:
            new_space = space + pace_space[next_pace]
            new_time = time + pace_time[next_pace]
            new_path = path + [next_pace]

            # Avoid going too far from target
            if p >= 0:
                if new_space > p + 20:
                    continue
            else:
                if new_space < p - 20:
                    continue

            queue.append((next_pace, new_space, new_time, new_path))

    return None

def verify_sequence(seq, p, t):
    """Verify if a sequence is valid"""
    if not seq:
        return False

    pace = 0
    space = 0
    time = 1  # Starting at pace 0 costs 1 time

    for next_pace in seq:
        # Check valid transition
        if next_pace not in transitions[pace]:
            print(f"Invalid transition: {pace} -> {next_pace}")
            return False

        pace = next_pace
        space += pace_space[pace]
        time += pace_time[pace]

    # Must end at pace 0
    if pace != 0:
        print(f"Does not end at pace 0, ends at {pace}")
        return False

    # Must reach exact position
    if space != p:
        print(f"Wrong position: got {space}, expected {p}")
        return False

    # Must be within time limit
    if time > t:
        print(f"Time exceeded: {time} > {t}")
        return False

    return True

def write_sol(sol, output_file):
    """Write solution to output file"""
    with open(output_file, "w") as file:
        for sequence in sol:
            if sequence == ["IMPOSSIBLE"]:
                file.write("IMPOSSIBLE\n")
            else:
                file.write(" ".join(map(str, sequence)) + "\n")

def parse(lines, input_file, output_file):
    """Parse input and generate solutions"""
    n = int(lines[0])
    lines = lines[1:n+1]

    sol = []

    for idx, line in enumerate(lines, 1):
        P, T = map(int, line.split())
        seq = find_sequence(P, T)

        if seq is None:
            seq = ["IMPOSSIBLE"]
            print(f"Case {idx}: P={P}, T={T} -> IMPOSSIBLE")
        else:
            valid = verify_sequence(seq, P, T)
            status = "✓" if valid else "✗"
            print(f"Case {idx}: P={P}, T={T} -> {' '.join(map(str, seq))} {status}")

        sol.append(seq)

    write_sol(sol, output_file)
    print(f"\nOutput written to: {output_file}")

def main():
    """Main function to process input files"""
    lvl = "3"

    # Change this to process different input files
    # 0: example, 1: small, 2: large
    cases_to_run = [2]  # Run example and small

    file_types = ["example", "small", "large"]
    file_numbers = ["0", "1", "2"]

    for case in cases_to_run:
        input_file = f"input/level{lvl}/level{lvl}_{file_numbers[case]}_{file_types[case]}.in"
        output_file = f"output/level{lvl}/level{lvl}_{file_numbers[case]}_{file_types[case]}.out"

        print(f"\n{'='*60}")
        print(f"Processing: {file_types[case].upper()}")
        print(f"{'='*60}")

        try:
            with open(input_file, "r") as file:
                lines = file.read().splitlines()
                parse(lines, input_file, output_file)
        except FileNotFoundError:
            print(f"Error: Could not find {input_file}")
        except Exception as e:
            print(f"Error processing {input_file}: {e}")

if __name__ == "__main__":
    main()
