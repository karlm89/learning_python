age = int(input("Enter your age: "))

if age < 2:
    print('Infant Ticket')
elif age >= 2 and age <= 8:
    print("Child ticket")
elif age >= 65:
    print('Senior Citizen ticket')
else:
    print('Adult ticket')