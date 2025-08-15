users = {"admin": "admin1234", "radical227": "happy123*4"}
active_friends = ["admin", "radical227"]

def login():
    username = input("Enter username: ").strip().lower()
    password = input("Enter password: ").strip()

    if username in users and users[username] == password:
        print(f"\nWelcome back, {username}!\n")
        return username, False  # old user
    else:
        print("Login failed. You can create a new account.")
        return create_account()

def create_account():
    username = input("Choose a username: ").strip().lower()
    password = input("Choose a password: ").strip()

    users[username] = password
    print(f"\nAccount '{username}' created!\n")
    return username, True  # new user

def old_user_menu(username):
    while True:
        print("\n1 - View Active Friends")
        print("2 - Logout")
        choice = input("Enter choice: ")

        if choice == "1":
            print("\nActive Friends:")
            for friend in active_friends:
                print("-", friend)
        elif choice == "2":
            print(f"Goodbye, {username}!\n")
            break
        else:
            print("Invalid choice!")

def new_user_menu(username):
    friends = []
    while True:
        print("\n1 - Add Friend")
        print("2 - View My Friends")
        print("3 - Logout")
        choice = input("Enter choice: ")

        if choice == "1":
            friend = input("Enter friend's name: ").strip()
            friends.append(friend)
            print(f"{friend} added to your list!")
        elif choice == "2":
            print("\nYour Friends:")
            for friend in friends:
                print("-", friend)
        elif choice == "3":
            print(f"Goodbye, {username}!\n")
            break
        else:
            print("Invalid choice!")

def main():
    username, is_new = login()
    if is_new:
        new_user_menu(username)
    else:
        old_user_menu(username)

if __name__ == "__main__":
    main()
