import sys
import time

users = {'admin': 'admin1234', 'radical227': 'happy123*4', 'ship44@': 'p@$$w0rd'}
active_friends = ['admin', 'radical227', 'ship44@']
new_friends = ['kelly3', 'cipher_dude27', 'nomago44@']

def login(users):
    attempts = 3
    while attempts > 0:
        username = input('Enter username: ').lower().strip()
        password = input('Enter password: ').lower().strip()
        if username in users:
            if users[username] == password:
                print(f'\nWelcome, {username}!\n')
                return username
            else:
                print('Wrong password. You can reset it.')
                if reset_password(users, username):
                    continue  # After reset, retry login
                else:
                    attempts -= 1
                    print(f'Attempts left: {attempts}\n')
        else:
            print('User not found. You may create a new account.')
            if create_account(users):
                print('Account created. Please login now.\n')
            else:
                attempts -= 1
                print(f'Attempts left: {attempts}\n')
    print('Too many failed attempts. Exiting...')
    sys.exit()

def reset_password(users, username):
    choice = input('Do you want to reset your password? (yes/no): ').lower().strip()
    if choice == 'yes':
        new_pass = input('Enter new password: ').strip()
        if new_pass:
            users[username] = new_pass
            print('Password updated successfully!\n')
            return True
        else:
            print('Password cannot be blank.')
    return False

def create_account(users):
    choice = input('Create new account? (yes/no): ').lower().strip()
    if choice == 'yes':
        while True:
            new_user = input('Enter new username: ').lower().strip()
            if not new_user:
                print('Username cannot be blank.')
                continue
            if new_user in users:
                print('Username already exists, try another.')
            else:
                break
        while True:
            new_pass = input('Enter new password: ').strip()
            if not new_pass:
                print('Password cannot be blank.')
            else:
                break
        users[new_user] = new_pass
        print(f'Account "{new_user}" created successfully!\n')
        return True
    return False

def show_active_friends():
    print('\nActive Friends:')
    for friend in active_friends:
        print(f'- {friend}')
    print()

def show_new_friends():
    print('\nNew Friends:')
    for friend in new_friends:
        print(f'- {friend}')
    print()

def main_menu(username):
    while True:
        print('Options:')
        print('1 - Show Active Friends')
        print('2 - Show New Friends')
        print('3 - Logout')
        choice = input('Enter your choice: ').strip()
        if choice == '1':
            show_active_friends()
        elif choice == '2':
            show_new_friends()
        elif choice == '3':
            print(f'Goodbye, {username}!\n')
            break
        else:
            print('Invalid choice. Please try again.\n')

def main():
    print('Welcome to the CLI App!\n')
    username = login(users)
    main_menu(username)
    print('Thank you for using the app!')

if __name__ == "__main__":
    main()
