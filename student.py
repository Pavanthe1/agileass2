students_data = {
    "Alice": {"Python": 85, "Mathematics": 92, "AI": 88},
    "Bob": {"Python": 78, "Mathematics": 35, "AI": 80},
    "Charlie": {"Python": 95, "Mathematics": 98, "AI": 96},
    "David": {"Python": 60, "Mathematics": 65, "AI": 58},
    "Eve": {"Python": 45, "Mathematics": 50, "AI": 38}
}

processed_results = {}
PASS_MARKS = 40

for name, marks in students_data.items():
    total = sum(marks.values())
    percentage = (total / 300) * 100
    
    if percentage >= 90:
        grade = 'A'
    elif percentage >= 80:
        grade = 'B'
    elif percentage >= 70:
        grade = 'C'
    elif percentage >= 50:
        grade = 'D'
    else:
        grade = 'F'
        
    processed_results[name] = {
        "marks": marks,
        "total": total,
        "percentage": round(percentage, 2),
        "grade": grade
    }

topper_name = max(processed_results, key=lambda x: processed_results[x]["percentage"])

failed_students = []
for name, info in processed_results.items():
    for subject, score in info["marks"].items():
        if score < PASS_MARKS:
            failed_students.append((name, subject, score))
            break

sorted_students = sorted(processed_results.items(), key=lambda x: x["percentage"], reverse=True)

print("--- Semester Results ---")
for name, info in processed_results.items():
    print(f"Student: {name} | Total: {info['total']}/300 | Percentage: {info['percentage']}% | Grade: {info['grade']}")

print("\n--- Class Topper ---")
print(f"Topper: {topper_name} with {processed_results[topper_name]['percentage']}%")

print("\n--- Students Who Failed in Any Subject (Pass Mark: 40) ---")
if failed_students:
    for name, subject, score in failed_students:
        print(f"Student: {name} failed in {subject} (Score: {score})")
else:
    print("No students failed.")

print("\n--- Students Sorted by Percentage (Highest to Lowest) ---")
for rank, (name, info) in enumerate(sorted_students, 1):
    print(f"{rank}. {name}: {info['percentage']}%")
