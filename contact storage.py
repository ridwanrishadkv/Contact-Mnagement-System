import os
from config import CONTACT_FILE

def load_contacts():
    contacts = {}
    if os.path.exists(CONTACT_FILE):
        with open(CONTACT_FILE, 'r') as f:
            for line in f:
                parts = line.strip().split('|')
                if len(parts) == 4:
                    phone = parts[0]
                    name = parts[1]
                    email = parts[2]
                    address = parts[3]
                    contacts[phone] = {"name": name, "email": email, "address": address}
    return contacts

def save_contacts(contacts):
    with open(CONTACT_FILE, 'w') as f:
        for phone, i in contacts.items():
            f.write(f"{phone}|{i['name']}|{i['email']}|{i['address']}\n")
