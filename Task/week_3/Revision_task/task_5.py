# Revision Task: 5. write a program to detect if there are double spaces in a string and replace the double space with a single space

s_input = input("Enter your string: ") 

def detectDoubleSpacr(s):
    if "  " in s:
        newS = s.replace("  "," ")
        print("Updated string:",newS)
    else:
        print("No double space detected.")

detectDoubleSpacr(s_input)