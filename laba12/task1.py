people_count = int(input("Введите количество людей: "))
people = {
    "woman and children": [], 
    "men": [], 
    "captain": None
}

for i in range(people_count):
    name, status = input("Введите данные о человеке: ").lower().split()

    if status in ["woman", "child"]:
        people["woman and children"].append(name.capitalize())
    elif status == "man":
        people["men"].append(name.capitalize())
    else:
        if people["captain"] != None:
            raise ValueError("There can't be more than 1 captain.")
            # print("There can't be more than 1 captain.")
            # break
        else:
            people["captain"] = name.capitalize()

for name in people["woman and children"]:
    print(name)

for name in people["men"]:
    print(name)

print(people["captain"])