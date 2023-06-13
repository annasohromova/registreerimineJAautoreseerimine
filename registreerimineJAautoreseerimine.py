from module1 import *

usernames = []
passwords = []
file_path = "salasona.txt"

while True:
    print("\nMenüü:")
    print("1. Registreeri")
    print("2. Autoriseeri")
    print("3. Andmete muutmine")
    print("4. Unustasid parooli")
    print("5. Välju")

    choice = input("Sisesta valik: ")

    if choice == "1":
        usernames, passwords = registration(usernames, passwords)
        save_dictionary(usernames, passwords, file_path)
    elif choice == "2":
        usernames, passwords = load_dictionary(file_path)
        authorized = authorization(usernames, passwords)
        if authorized:
            print("Autoriseerimine õnnestus!")
        else:
            print("Autoriseerimine ebaõnnestus!")
    elif choice == "3":
        usernames, passwords = load_dictionary(file_path)
        usernames, passwords = change_credentials(usernames, passwords)
        save_dictionary(usernames, passwords, file_path)
    elif choice == "4":
        usernames, passwords = load_dictionary(file_path)
        usernames, passwords = forgot_password(usernames, passwords)
        save_dictionary(usernames, passwords, file_path)
    elif choice == "5":
        print("Head aega!")
        break
    else:
        print("Vigane valik! Palun proovi uuesti.")

