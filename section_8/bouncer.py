age = int(input("How old are you? "))

if age >= 18 and age < 21:
    print('You can enter, but cannot drink')
elif age >= 21:
    print('You can enter, and drink!')
else:
    print('You cannot enter, or drink')