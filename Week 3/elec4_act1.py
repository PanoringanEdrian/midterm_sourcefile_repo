# Week 3 - Lesson 1 - Hands-on Exercise

scores = []

# a. Input student scores
while True:
    score = input("Score: ")
    if score == "":
        break
    scores.append(int(score))

print()

# b. Display all students scores
print("Student Scores:")
for score in scores:
    print(score)

print()

# c. Check each student's grade and pass/fail status
total = 0
passed = 0
failed = 0
number = 1

for score in scores:
    total = total + score

    if score >= 90:
        grade = "Excellent"
    elif score >= 80:
        grade = "Very Good"
    elif score >= 75:
        grade = "Good"
    else:
        grade = "Failed"

    if score >= 75:
        status = "Passed"
        passed = passed + 1
        print("Student " + str(number) + ": " + str(score) + " - " + grade + " - " + status)
    else:
        status = "Failed"
        failed = failed + 1
        print("Student " + str(number) + ": " + str(score) + " - " + status)

    number = number + 1

print()

# d. Total score
print("Total Score: ", total)

# e. Average score
average = total / len(scores)
print("Average Score: ", round(average))

# f. Highest score
highest = max(scores)
print("Highest Score: ", highest)

# g. Lowest score
lowest = min(scores)
print("Lowest Score: ", lowest)

# h.Number of students who passed
print("Passed: ", passed)

# i. Number of students who failed
print("Failed: ", failed)