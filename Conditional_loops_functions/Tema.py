max_attempts = 5
attempt = 1

while attempt <= max_attempts:

    try:
        user_age = int(input('user_age: '))
    except ValueError:
        print("Invalid age. Try again. Only use numbers.")
        attempt += 1
        continue

    if user_age >= 18:
        print("You are a grown up!")
    else:
        print("You are a child!")
    break

else:
    print("You have exceeded the maximum number of attempts. (5 attempts)")