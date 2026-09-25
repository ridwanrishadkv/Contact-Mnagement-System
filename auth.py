from user_storage import load_users, save_users

def authenticate():
    users = load_users()
    print("\n=== Authentication ===")
    print("1. Login\n2. Register")
    choice = input("Choose (1-2): ").strip()
    username = input("Enter Username: ").strip()
    password = input("Enter Password: ").strip()
    
    if choice == '2':
        if username in users:
            print("\n User already exists. Try logging in.")
        else:
            users[username] = password
            save_users(users)
            print("\n Registration successful! Please log in.")
        return authenticate()
    
    if users.get(username) == password:
        print(f"\n Welcome back, {username}!")
        return True
    
    print("\n Invalid username or password.")
    return authenticate()
