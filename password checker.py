def password_checker():
    password = input("Enter your password: ")

    if len(password) < 8:
        print("Password too short. It must be at least 8 characters.")
        return

    if not any(char.isdigit() for char in password):
        print("Password must contain at least one number.")
        return
    
    if not any(char.isupper() for char in password):
        print("Password must contain at least one upper.")
        return

    if not any(char.islower() for char in password):
        print("Password must contain at least one lower.")
        return

    special_symbols = "!@#$"
    if not any(char in special_symbols for char in password):
        print(f"Password must contain at least one special symbol ({special_symbols}).")
        return

    print("Password is valid!")

password_checker()

