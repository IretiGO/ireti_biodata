# Biodata assignment - Ireti


users = {}
SECRET = "stop"

count = 0

while count < 10:
    name = input("Enter name (or type 'stop' to exit): ")

    if name == SECRET:
        break

    age = int(input("Enter age: "))
    gender = input("Enter gender: ")

    # Determine the age category
    if age >= 3 and age <= 12:
        category = "child"
    elif age >= 13 and age <= 19:
        category = "teenager"
    elif age >= 20 and age <= 39:
        category = "young adult"
    elif age >= 40 and age <= 64:
        category = "middle aged"
    elif age >= 65:
        category = "senior"
    else:
        category = "unknown"

    # Store in dictionary
    users[name] = [age, category, gender]

    count = count + 1

print(users)
