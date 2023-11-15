age = "how old are you?"
while True:
    age = input(age)
    if age == 'quit':
        break
    age = int(age)
    if age < 3 :
        print("The ticket is free for you")
    elif age < 13 :
        print("The ticket will cost you $10")
    else:
        print("The ticket will cost you $15")