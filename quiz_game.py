print("Welcome to the Quiz Game!")

name = input("Enter your name: ")
print("Hello", name, "! Let's start the quiz.\n")

score = 0

# Question 1
answer1 = input("Q1: What is 2 + 2? ")
if answer1 == "4":
    print("Correct!\n")
    score = score + 1
else:
    print("Wrong! Correct answer is 4.\n")

# Question 2
answer2 = input("Q2: What color is the sky on a clear day? ")
if answer2.lower() == "blue":
    print("Correct!\n")
    score = score + 1
else:
    print("Wrong! Correct answer is Blue.\n")

# Question 3
answer3 = input("Q3: How many days are there in a week? ")
if answer3 == "7":
    print("Correct!\n")
    score = score + 1
else:
    print("Wrong! Correct answer is 7.\n")

print(name, ", your final score is:", score, "/ 3")

if score == 3:
    print("Excellent! You got all correct!")
elif score == 2:
    print("Good job! Almost perfect.")
elif score == 1:
    print("You can do better. Keep practicing!")
else:
    print("Try again. Better luck next time!")
