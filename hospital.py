patients = [
    {"Name": "Alice", "Age": 45, "Heart Rate": 72, "Oxygen Saturation": 98},
    {"Name": "Bob", "Age": 62, "Heart Rate": 105, "Oxygen Saturation": 96},
    {"Name": "Charlie", "Age": 50, "Heart Rate": 58, "Oxygen Saturation": 93},
    {"Name": "Diana", "Age": 35, "Heart Rate": 110, "Oxygen Saturation": 91}
]

print("--- All Patient Details ---")
for p in patients:
    print(f"Name: {p['Name']}, Age: {p['Age']}, Heart Rate: {p['Heart Rate']}, O2 Saturation: {p['Oxygen Saturation']}%")

print("\n--- Patient Classification ---")
critical_patients = []
for p in patients:
    hr = p["Heart Rate"]
    o2 = p["Oxygen Saturation"]
    
    if o2 < 95:
        status = "Critical"
        critical_patients.append(p)
    elif hr < 60 or hr > 100:
        status = "Observation"
    else:
        status = "Normal"
        
    print(f"{p['Name']}: {status}")

print("\n--- Critical Patients ---")
for p in critical_patients:
    print(f"Name: {p['Name']}, Age: {p['Age']}")

print("\n--- Average Age of Critical Patients ---")
if critical_patients:
    avg_age = sum(p["Age"] for p in critical_patients) / len(critical_patients)
    print(f"Average Age: {avg_age:.2f}")
else:
    print("No critical patients.")

print("\n--- Sorted by Oxygen Saturation (Ascending) ---")
sorted_patients = sorted(patients, key=lambda x: x["Oxygen Saturation"])
for p in sorted_patients:
    print(f"{p['Name']}: {p['Oxygen Saturation']}%")
