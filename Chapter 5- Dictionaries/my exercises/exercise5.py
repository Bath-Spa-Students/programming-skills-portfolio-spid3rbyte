pet_1 = {
    'owners name':"Jennie",
    'pet type':"cat",
    'pet species':"ragdoll"
    }

pet_2 = {
    'owners name':"Malika",
    'pet type': "dog",
    'pet species': "golden retriever"
    }

pets = []
pets.append(pet_1)
pets.append(pet_2)
for pet in pets:
    print("Everything about this pet: ")
    for key, value in pet.items():
        print(key + ": " + value)