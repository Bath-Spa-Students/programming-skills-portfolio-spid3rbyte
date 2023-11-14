rivers = {
    'mississippi river': 'united states',
    'nile river':'egypt', 
    'mekong river':'thailand', 
}
for river, country in rivers.items():
    print("The " + river.title() + " runs through " + country) 

print("The name of each river in this dictionary:")
for river in rivers.keys():
    print(river.title())

print("The name of each country in this dictionary:")
for country in rivers.values():
    print(country.title())

    