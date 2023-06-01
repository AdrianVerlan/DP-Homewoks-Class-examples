data = [10,10,20,30]

try:
    index = int(input("Enter the index: "))
    value = data[index]
    print(f'The selected value is {value}')
except ValueError:
    print("You must write an integer!")
except IndexError:
    print("The index must be within range! ")
finally:
    print("Thanks for ussing this app! ")