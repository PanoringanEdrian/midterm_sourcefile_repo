"""
Student Grade Analyzer - Version 3

"""

# f. add guardian conditions
raw_records = [
    "Ana,88,92,90",
    "Ben,70,72,74",
    "Cara,95,91,94",
    "Dan,78,80,76",
    "Ella,85,89,87",
    "Fred,90,85",
    "Gina",
    "Henry,90,eighty,85",
    "Ivy,",
]

PASSING_GRADE = 75
student_scores = {}


# a. Parse raw records into student_scores
for record in raw_records:
    fields = record.split(",")

    if len(fields) != 4:
        print(f"Skipped invalid record: {record}")
        continue

    name = fields[0]
    score_fields = fields[1:]

    try:
        scores = [float(score) for score in score_fields]
    except ValueError:
        print(f"Skipped invalid record: {record}")
        continue

    student_scores[name] = scores


# b. display parsed records, sorted alphabetically by name

print("\nORGANIZED STUDENT RECORDS")
for name in sorted(student_scores.keys()):
    print(f"{name}: {student_scores[name]}")


# c. Compute results (total, average, highest, lowest, remark)

ranking = []
passed_count = 0
failed_count = 0
sum_of_averages = 0

for name, scores in student_scores.items():
    if not scores:  # guard against an empty score list
        continue

    total = sum(scores)
    average = total / len(scores)
    highest_score = max(scores)
    lowest_score = min(scores)
    remark = "Passed" if average >= PASSING_GRADE else "Failed"

    if remark == "Passed":
        passed_count += 1
    else:
        failed_count += 1

    sum_of_averages += average
    ranking.append((average, name, highest_score, lowest_score, remark))


# d. Sort and display the ranking (highest average first)

ranking.sort(key=lambda item: item[0], reverse=True)

print("\nSTUDENT GRADE REPORT")
print("Rank  Name       Average  Highest  Lowest  Remark")

for rank, (average, name, highest, lowest, remark) in enumerate(ranking, start=1):
    print(f"{rank:<6}{name:<11}{average:<9.2f}{highest:<9.0f}{lowest:<8.0f}{remark}")


# e. Class summary

class_average = sum_of_averages / len(ranking) if ranking else 0

print("\nCLASS SUMMARY")
print(f"Number of Students: {len(ranking)}")
print(f"Passed: {passed_count}")
print(f"Failed: {failed_count}")
print(f"Class Average: {class_average:.2f}")

if ranking:
    highest_student = ranking[0]
    lowest_student = ranking[-1]
    print(f"Highest: {highest_student[1]} - {highest_student[0]:.2f}")
    print(f"Lowest: {lowest_student[1]} - {lowest_student[0]:.2f}")
else:
    print("Highest: N/A")
    print("Lowest: N/A")