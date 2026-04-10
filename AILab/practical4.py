from collections import deque

# Goal State
goal = [1,2,3,4,5,6,7,8,0]

# Function to find index of zero
def find_zero(state):
    return state.index(0)

# Function to generate new states
def generate_states(state):
    new_states = []
    zero_index = find_zero(state)

    # Possible moves (up, down, left, right)
    moves = {
        "up": -3,
        "down": 3,
        "left": -1,
        "right": 1
    }

    for move, position in moves.items():

        new_index = zero_index + position

        # Check valid move
        if move == "left" and zero_index % 3 == 0:
            continue
        if move == "right" and zero_index % 3 == 2:
            continue
        if 0 <= new_index < 9:
            new_state = state.copy()

            # Swap values
            new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]

            new_states.append(new_state)

    return new_states


# BFS Algorithm
def solve_puzzle(initial):

    queue = deque([initial])
    visited = []

    while queue:

        state = queue.popleft()

        print(state)

        if state == goal:
            print("Goal State Reached!")
            return

        visited.append(state)

        for next_state in generate_states(state):
            if next_state not in visited:
                queue.append(next_state)


# Initial State
initial_state = [1,2,3,4,0,5,6,7,8]

# Function call
solve_puzzle(initial_state)
