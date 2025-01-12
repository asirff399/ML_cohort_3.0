# Video 6 Task 2
# Find lowest CGPA
f1_CGPA = float(input("Enter first friend CGPA: "))
f2_CGPA = float(input("Enter second friend CGPA: "))
f3_CGPA = float(input("Enter third friend CGPA: "))

if f1_CGPA<f2_CGPA and f1_CGPA<f3_CGPA:
    print("First friend got lowest CGPA")
elif f2_CGPA<f1_CGPA and f2_CGPA<f3_CGPA:
    print("Second friend got lowest CGPA")
else:
    print("Third friend got lowest CGPA")

# Average CGPA
averageCGPA = (f1_CGPA+f2_CGPA+f3_CGPA) / 3
print(f"Average CGPA between them: {averageCGPA}")