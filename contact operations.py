import sys
from contact_storage import load_contacts, save_contacts

def get_phone_input(prompt_text):
    while True:
        phone = input(prompt_text).strip()
        if phone.isdigit():
            return phone
        print("\n Invalid input. Phone number must contain digits only.")

def run_contact_system():
    contacts = load_contacts()
    while True:
        print("\n=== Contact Management System ===")
        print("1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Delete Contact\n5. Exit")
        choice = input("Enter choice (1-5): ").strip()
        if choice == '1':
            name = input("Name: ").strip()
            if not name:
                print("\n[!] Name is required.")
                continue
            phone = get_phone_input("Phone (digits only): ")
            email = input("Email: ").strip()
            address = input("Address: ").strip()
            contacts[phone] = {"name": name, "email": email, "address": address}
            save_contacts(contacts)
            print(f"\n Contact '{name}' added successfully.")   
        elif choice == '2':
            if not contacts:
                print("\n Address book is empty.")
            else:
                print("\n--- Contact List ---")
                for phone, i in contacts.items():
                    print(f"Name: {i['name']:<15} | Phone: {phone:<10} | Email: {i['email']}")
                    
        elif choice == '3':
            phone = get_phone_input("Enter Phone to search: ")
            c = contacts.get(phone)
            if c:
                print(f"\n Found -> Name: {c['name']} | Email: {c['email']} | Address: {c['address']}")
            else:
                print("\n Contact not found.")
                
        elif choice == '4':
            phone = get_phone_input("Enter Phone to delete: ")
            if contacts.pop(phone, None):
                save_contacts(contacts)
                print("\n Contact deleted.")
            else:
                print("\n Contact not found.")
                
        elif choice == '5':
            print("\nGoodbye!")
            sys.exit()
        else:
            print("\n Invalid choice.")
