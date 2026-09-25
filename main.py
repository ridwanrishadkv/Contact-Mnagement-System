from auth import authenticate
from contact_operations import run_contact_system

def main():
    if authenticate():
        run_contact_system()

if __name__ == "__main__":
    main()
