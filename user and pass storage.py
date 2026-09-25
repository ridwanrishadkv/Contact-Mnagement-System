import os
from config import USER_FILE

def load_users():
    users = {}
    if os.path.exists(USER_FILE):
        with open(USER_FILE, 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    users[parts[0]] = parts[1]
    return users

def save_users(users):
    with open(USER_FILE, 'w') as f:
        for user, pwd in users.items():
            f.write(f"{user},{pwd}\n")
