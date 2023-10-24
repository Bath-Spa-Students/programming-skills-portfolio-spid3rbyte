dinner_people =  ["Mahmoud Darwish", "Shefale Akther", "Alisha Rizwan"]
dinner_1 = dinner_people[0]+ " please join my dinner" 
print(dinner_1)
dinner_2 = dinner_people[1]+ " please join my dinner" 
print(dinner_2)
dinner_3 = dinner_people[2]+ " please join my dinner" 
print(dinner_3)

print(dinner_people[0] + " can't make it to dinner :(")

dinner_people[0]="Naznin Jamshed"

dinner_1 = dinner_people[0]+ " please join my dinner" 
print(dinner_1)
dinner_2 = dinner_people[1]+ " please join my dinner" 
print(dinner_2)
dinner_3 = dinner_people[2]+ " please join my dinner" 
print(dinner_3)

print("I can only invite two people to my dinner")

print("Sorry " + dinner_people[1] + " I can't invite you")
dinner_people.pop(1)

invitation = dinner_people[0]+ " you're still invited to my dinner <3"
print(invitation)
invitation_2 = dinner_people[1]+ " you're still invited to my dinner <3"
print(invitation_2)

del(dinner_people[0])
del(dinner_people[0])
print(dinner_people)