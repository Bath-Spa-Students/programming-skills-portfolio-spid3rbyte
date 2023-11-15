topping = "Enter pizza topping you'd like"
quit = "Enter quit when you're done"
print(quit)
while True:
    topping = input(topping)
    if topping != 'quit':
        print("I'll add " + topping + " to your pizza")
    else:
        break