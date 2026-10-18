
import json

file = "contacts.json"


def load_contacts():
    try:
        with open(file, "r") as f:
            contacts = json.load(f)

            if isinstance(contacts, list):
                if all(
                    isinstance(contact, dict)
                    and all(
                        isinstance(contact.get(key), str)
                        for key in ("name", "phone", "email")
                    )
                    for contact in contacts
                ):
                    return contacts

            return []

    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_contacts(contacts):
    with open(file, "w") as f:
        json.dump(contacts, f)


def add_contact(contacts):
    print("\n--- Add Contact ---")

    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    if not name:
        print("Name cannot be empty.")
        return

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    save_contacts(contacts)

    print("Contact added successfully!")


def list_contacts(contacts):
    print("\n--- Contact List ---")

    if not contacts:
        print("No contacts found.")
        return

    for index, contact in enumerate(contacts, start=1):
        print(f"\nContact {index}")
        print(f"Name: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")


def search_contact(contacts):
    print("\n--- Search Contact ---")

    search_name = input("Enter all or part of the name: ").casefold()

    if not search_name:
        print("Please enter a name to search.")
        return

    found = False

    for contact in contacts:
        if search_name in contact["name"].casefold():
            print(f"\nName: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            found = True

    if not found:
        print("No matching contacts found.")


def edit_contact(contacts):
    print("\n--- Edit Contact ---")

    search_name = input("Enter all or part of the name: ").casefold()

    if not search_name:
        print("Please enter a name to search.")
        return

    matches = [
        contact for contact in contacts
        if search_name in contact["name"].casefold()
    ]

    if not matches:
        print("No matching contacts found.")
        return

    for index, contact in enumerate(matches, start=1):
        print(f"{index}. {contact['name']} - {contact['phone']}")

    try:
        choice = int(input("Choose the contact number to edit: "))

        if choice < 1 or choice > len(matches):
            print("Invalid contact number.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    contact = matches[choice - 1]

    name = input(f"New name [{contact['name']}]: ")
    phone = input(f"New phone [{contact['phone']}]: ")
    email = input(f"New email [{contact['email']}]: ")

    if name:
        contact["name"] = name

    if phone:
        contact["phone"] = phone

    if email:
        contact["email"] = email

    save_contacts(contacts)
    print("Contact updated successfully!")


def delete_contact(contacts):
    print("\n--- Delete Contact ---")

    search_name = input("Enter all or part of the name: ").casefold()

    if not search_name:
        print("Please enter a name to search.")
        return

    matches = [
        contact for contact in contacts
        if search_name in contact["name"].casefold()
    ]

    if not matches:
        print("No matching contacts found.")
        return

    for index, contact in enumerate(matches, start=1):
        print(f"{index}. {contact['name']} - {contact['phone']}")

    try:
        choice = int(input("Choose the contact number to delete: "))

        if choice < 1 or choice > len(matches):
            print("Invalid contact number.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    contact = matches[choice - 1]

    confirm = input(
        f"Delete {contact['name']}? (y/n): "
    ).lower()

    if confirm == "y":
        contacts.remove(contact)
        save_contacts(contacts)
        print("Contact deleted successfully!")
    else:
        print("Deletion cancelled.")


def main():
    contacts = load_contacts()

    while True:
        print("\n===== CONTACT BOOK =====")
        print("1. Add contact")
        print("2. List contacts")
        print("3. Search contact")
        print("4. Edit contact")
        print("5. Delete contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contacts)

        elif choice == "2":
            list_contacts(contacts)

        elif choice == "3":
            search_contact(contacts)

        elif choice == "4":
            edit_contact(contacts)

        elif choice == "5":
            delete_contact(contacts)

        elif choice == "6":
            print("Contacts saved. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1 to 6.")


if __name__ == "__main__":
    main()
