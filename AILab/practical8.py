# Initial positions
monkey = "A"
box = "B"
banana = "C"

def monkey_banana():

    print("Initial State:")
    print("Monkey at:", monkey)
    print("Box at:", box)
    print("Banana at:", banana)
    print()

    # Step 1: Monkey moves to box
    print("Monkey moves from", monkey, "to", box)

    # Step 2: Monkey pushes box to banana position
    print("Monkey pushes box from", box, "to", banana)

    # Step 3: Monkey climbs the box
    print("Monkey climbs the box")

    # Step 4: Monkey grasps the banana
    print("Monkey grasps the banana")

    print("\nGoal Achieved: Monkey got the banana!")


# Function call
monkey_banana()
