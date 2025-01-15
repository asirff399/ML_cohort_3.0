# Video 9-10 Task 3: Dictionaries
# Write a program that:

# 1. Creates a dictionary where keys are subject names (e.g., Math, Science) and values are the marks (e.g., 90, 85).
result = {
    "Bangla":83,
    "English":87,
    "Math":90,
    "ICT":97,
}

# 2. Adds a new subject with its mark to the dictionary.
result["Science"] = 91

# 3. Updates the mark for one subject.
result["Bangla"] = 84
# print(result)

# 4. Prints the average marks.
total_mark = 0
for sub,mark in result.items():
    total_mark+=mark
average = total_mark/len(result)
print(average)
