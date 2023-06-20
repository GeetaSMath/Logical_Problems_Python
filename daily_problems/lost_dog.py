# Find the Lost Dog
# 0 represents the dog.
# Each list represents a house and each 1 represents an empty room.
# Return the house and the room where it is located, there can be only one dog lost per building.
# Examples
# lost_dog([1, 1, 1, 1, 1, 1],  [1, 1, 1, 1, 1, 1],  [1, 1, 1, 1, 1, 1],  [1, 1, 1, 1, 1, 1])
# ➞ "Dog not found!"
#
# lost_dog([1, 1, 1, 1, 1, 1],  [0, 1, 1, 1, 1, 1],  [1, 0, 1, 1, 1, 1],  [1, 1, 1, 1, 1, 1])
# ➞ {"Dog1": "House (2) and Room (1)", "Dog2": "House (3) and Room (2)"}
# lost_dog([1, 1, 1, 1, 1, 0],  [0, 1, 1, 1, 1, 1],  [1, 0, 1, 1, 1, 1],  [1, 1, 0, 1, 1, 1])
# ➞ {"Dog1": "House (1) and Room (6)", "Dog2": "House (2) and Room (1)",
#    "Dog3": "House (3) and Room (2)", "Dog4": "House (4) and Room (3)"}


def lost_dog(*houses):
    dog_location = {}
    dog_count = 1

    for i, house in enumerate(houses, start=1):
        if 0 in house:
            room = house.index(0) + 1
            dog_location[f"Dog{dog_count}"] = f"House ({i}) and Room ({room})"
            dog_count += 1
    if len(dog_location) == 0:
        return "Dog not found!"
    else:
        return dog_location


house1 = [1, 1, 1, 1, 1, 1]
house2 = [1, 1, 1, 1, 1, 1]
house3 = [1, 1, 1, 1, 1, 1]
house4 = [1, 1, 1, 1, 1, 1]
print(lost_dog(house1, house2, house3, house4))

house1 = [1, 1, 1, 1, 1, 1]
house2 = [0, 1, 1, 1, 1, 1]
house3 = [1, 0, 1, 1, 1, 1]
house4 = [1, 1, 1, 1, 1, 1]
print(lost_dog(house1, house2, house3, house4))
