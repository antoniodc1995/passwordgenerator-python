import random
password = "ABCDEFGHIJKLMNOPQRSTUVWYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+{}:<>"

max_length = len(password)

while True:
    try:
        length_password = int(input(f"Enter the length of the password (1-{max_length}): "))
        if 1 <= length_password <= max_length:
            break
        else:
            print(f"Please enter a number between 1 and {max_length}.")
    except ValueError:
        print("Please enter a valid integer.")

a= "".join(random.sample(password, length_password))
print(f"Your password is: {a}")