class PasswordManager:
    def __init__(self):
        self.data = []  # List to store password entries

    def add_password(self, app, username, password):
        self.data.append({
            "app": app,
            "username": username,
            "password": password
        })
        print(f"✅ Password saved for '{app}'.")

    def view_passwords(self):
        if not self.data:
            print("🔐 No passwords saved.")
        else:
            for entry in self.data:
                print(f"\n📱 App: {entry['app']}")
                print(f"👤 Username: {entry['username']}")
                print(f"🔑 Password: {entry['password']}")

    def search_password(self, app):
        found = False
        for entry in self.data:
            if entry['app'].lower() == app.lower():
                print(f"\n🔎 Found: {entry['app']}")
                print(f"👤 Username: {entry['username']}")
                print(f"🔑 Password: {entry['password']}")
                found = True
        if not found:
            print("❌ No entry found for that app.")


# Main app
manager = PasswordManager()

while True:
    print("\n--- Password Manager ---")
    print("1. Add new password")
    print("2. View all passwords")
    print("3. Search password by app")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        app = input("Enter app/site name: ")
        username = input("Enter username/email: ")
        password = input("Enter password: ")
        manager.add_password(app, username, password)

    elif choice == "2":
        manager.view_passwords()

    elif choice == "3":
        app = input("Enter app/site name to search: ")
        manager.search_password(app)

    elif choice == "4":
        print("👋 Exiting Password Manager.")
        break

    else:
        print("❗ Invalid choice. Try again.")
