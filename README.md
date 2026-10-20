# Code Ninja Pro | Python Maths Quiz

**Make Times Tables Fun with Python!**

Build a simple multiplication quiz, test your maths skills, and learn to code through fun, hands-on projects.

🎯 **Age:** 9–10+  
⏱️ **Time:** 20 minutes  
💻 **Language:** Python  
🚀 **Level:** Beginner

## ✨ What You'll Learn
- 🎲 Generate random multiplication questions
- 🔁 Use loops to repeat questions
- ✅ Check answers with `if/else`
- 🏆 Track scores and challenge yourself

## 💻 Let's Code!

```python
import random

score = 0

for _ in range(5):
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    answer = input(f"{a} x {b} = ")

    if answer == str(a * b):
        score += 1
        print("Correct! 🎉")
    else:
        print(f"Oops! The answer is {a * b}")

print(f"You scored {score}/5!")
```

## 🚀 Level Up!
Ready for a challenge?

1. Add more questions.
2. Practise a specific times table.
3. Add difficulty levels and a timer.
4. Create a high-score system.

## 🥷 Learn. Build. Innovate.

At **[Code Ninja Pro](https://codeninja.pro)**, kids turn ideas into real projects through coding, AI, and robotics.

🎓 **Ready for your coding adventure?**

👉 [Book a Free Trial Class](https://codeninja.pro/free-trial)

⭐ Star this repository and start coding today!
