def get_grade(percentage):
    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 70:
        return 'C'
    elif percentage >= 60:
        return 'D'
    else:
        return 'F'

def process_results():
    # INTERNAL PROGRAM INPUTS (No more input() prompts)
    student_inputs = [
        "Alice 85 92 78",
        "Bob 35 75 80",
        "Charlie 95 88 91"
    ]
    
    students = {}

    for user_input in student_inputs:
        line = user_input.split()
        if len(line) < 4:
            print(f"Error: Invalid data format for '{user_input}'. Expected 4 values.")
            continue
            
        name = line[0]
        try:
            python = float(line[1])
            maths = float(line[2])
            ai = float(line[3])
        except ValueError:
            print(f"Error: Marks must be numerical values in '{user_input}'.")
            continue
        
        total = python + maths + ai
        percentage = total / 3.0
        grade = get_grade(percentage)
        failed = python < 40 or maths < 40 or ai < 40
        
        students[name] = {
            'marks': {'Python': python, 'Mathematics': maths, 'AI': ai},
            'total': total,
            'percentage': percentage,
            'grade': grade,
            'failed': failed
        }

    print("\n--- Student Results ---")
    for name, data in students.items():
        print(f"Name: {name} | Total: {data['total']:.2f} | Percentage: {data['percentage']:.2f}% | Grade: {data['grade']}")

    if students:
        topper = max(students, key=lambda k: students[k]['percentage'])
        print(f"\nClass Topper: {topper} with {students[topper]['percentage']:.2f}%")

    print("\nStudents who failed in any subject:")
    has_failed = False
    for name, data in students.items():
        if data['failed']:
            print(f"- {name}")
            has_failed = True
    if not has_failed:
        print("None")

    print("\nStudents Sorted by Percentage (Highest to Lowest):")
    sorted_students = sorted(students.items(), key=lambda item: item['percentage'], reverse=True)
    for name, data in sorted_students:
        print(f"- {name}: {data['percentage']:.2f}%")

if __name__ == "__main__":
    process_results()
