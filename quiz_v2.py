import random
import time

level = input("Choose level (easy/hard): ")
top = 9 if level == "easy" else 12

score = 0
start = time.time()
for _ in range(5):
    a, b = random.randint(2, top), random.randint(2, top)
    answer = input(f"{a} x {b} = ")
    if answer == str(a * b):
        score += 1
        print("Correct!")
    else:
        print(f"Oops, it's {a * b}")
seconds = round(time.time() - start)
print(f"You scored {score}/5 in {seconds} seconds")
