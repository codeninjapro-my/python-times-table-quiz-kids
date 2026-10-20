import random

score = 0
for _ in range(5):
    a, b = random.randint(2, 9), random.randint(2, 9)
    answer = input(f"{a} x {b} = ")
    if answer == str(a * b):
        score += 1
        print("Correct!")
    else:
        print(f"Oops, it's {a * b}")
print(f"You scored {score}/5")
