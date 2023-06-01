current_year = 2023
try:
    in_value = input("Enter your birth year: ")
    birth_year = int(in_value)
    age = current_year - birth_year
    print(f'You are {age} years old! ')
except:
    print("Error! Wrong age number")
