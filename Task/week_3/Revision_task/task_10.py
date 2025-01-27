# Revision Task: 10. create an empty dictionary, allow 4 friends to enter their favourite programming language as values and keys as their name. and display them. assume the names are unique

dictionary = {}

for i in range(4):
    name = input(f"Enter {i+1} friend name: ")
    language = input(f'Enter {name} favourite programming language: ')
    dictionary[name] = language

print("4 friends favourite programming language list:")
for name,language in dictionary.items():
    print(f"{name} favourite programming language is -> {language}")
