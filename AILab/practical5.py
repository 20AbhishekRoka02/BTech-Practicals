from collections import deque

# Jug capacities
jug1_capacity = 4
jug2_capacity = 3

# Target amount
target = 2

def water_jug_bfs():

    visited = set()
    queue = deque([(0, 0)])  # initial state

    while queue:

        jug1, jug2 = queue.popleft()

        print((jug1, jug2))

        # Check goal
        if jug1 == target or jug2 == target:
            print("Target reached!")
            return

        if (jug1, jug2) in visited:
            continue

        visited.add((jug1, jug2))

        # Possible states
        next_states = [
            (jug1_capacity, jug2), # Fill Jug1
            (jug1, jug2_capacity), # Fill Jug2
            (0, jug2),             # Empty Jug1
            (jug1, 0),             # Empty Jug2
            # Pour Jug1 -> Jug2
            (jug1 - min(jug1, jug2_capacity - jug2),
             jug2 + min(jug1, jug2_capacity - jug2)),
            # Pour Jug2 -> Jug1
            (jug1 + min(jug2, jug1_capacity - jug1),
             jug2 - min(jug2, jug1_capacity - jug1))
        ]

        for state in next_states:
            if state not in visited:
                queue.append(state)


# Function call
water_jug_bfs()
