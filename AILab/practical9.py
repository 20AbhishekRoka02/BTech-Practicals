from collections import deque

# Check if state is valid
def is_valid(m_left, c_left):
    m_right = 3 - m_left
    c_right = 3 - c_left

    # Missionaries should not be outnumbered by cannibals
    if (m_left > 0 and m_left < c_left):
        return False

    if (m_right > 0 and m_right < c_right):
        return False

    return True


def missionaries_cannibals():

    # (missionaries_left, cannibals_left, boat_position)
    start = (3, 3, 0)  # 0 = left, 1 = right
    goal = (0, 0, 1)

    queue = deque([start])
    visited = set()

    while queue:

        state = queue.popleft()
        m_left, c_left, boat = state

        print(state)

        if state == goal:
            print("Goal Reached!")
            return

        if state in visited:
            continue

        visited.add(state)

        moves = [
            (1,0), (2,0), # missionaries
            (0,1), (0,2), # cannibals
            (1,1)         # both
        ]

        for m, c in moves:

            if boat == 0:  # boat on left side
                new_state = (m_left-m, c_left-c, 1)
            else:  # boat on right side
                new_state = (m_left+m, c_left+c, 0)

            m_new, c_new, _ = new_state

            if 0 <= m_new <= 3 and 0 <= c_new <= 3 and is_valid(m_new, c_new):
                queue.append(new_state)


# Function call
missionaries_cannibals()
