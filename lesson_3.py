# Finger Exercise 3
"""
N = input("Insert the number of times you want to repeat this loop: ")

N = int(N)
for i in range(N):
    print("Hello World!")
"""

# Finger Exercise 3

N = input("Insert the number you want to find the root of: ")

N = int(N)

cube_root = round(N ** (1 / 3))

# Finger Exercise 4

if cube_root ** 3 == N:
    print(f"{N} is a perfect cube.")
    print(f"Cube root: {cube_root}")
else:
    print(f"{N} is not a perfect cube.")
    print(f"Approximate cube root: {N ** (1 / 3)}")