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
    students = {}
    
    n = int(input())
    for _ in range(n):
        line = input().split()
        name = line[0]
        python = float(line[1])
        maths = float(line[2])
        ai = float(line[3])
        
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
    
    print("--- Student Results ---")
    for name, data in students.items():
        print(f"Name: {name} | Total: {data['total']:.2f} | Percentage: {data['percentage']:.2f}% | Grade: {data['grade']}")
    
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
    sorted_students = sorted(students.items(), key=lambda item: item[1]['percentage'], reverse=True)
    for name, data in sorted_students:
        print(f"- {name}: {data['percentage']:.2f}%")

if __name__ == "__main__":
    process_results()
