from all_neos import all_neos
from large_neos import show_large_neos

API_KEY = "ibao9Xte7MmWeJG8TdVq07bfA85pNKWFeTUzwwwA"

def main_menu():
    while True:
        print("Welcome to NASA Near Earth Objects (NEO) explorer! 🚀")
        choice = input("""
        Please choose one of the following options below to continue:
                       
        1️⃣. List all NEOs from the last 4 weeks
        2️⃣. Show potentially hazardous NEOs
        3️⃣. Show large NEOs (>50m)
        4️⃣4. Exit
        """).strip()

        if choice == "1":
            print("Listing all NEOs from the last 4 weeks...")
            all_neos()
            input("\nPress Enter to return to the main menu...")

        elif choice == "2":
            print("Showing potentially hazardous NEOs...")
            input("\nPress Enter to return to the main menu...")

        elif choice == "3": 
            print("Showing large NEOs (>50m)...")
            show_large_neos(all_neos)
            input("\nPress Enter to return to the main menu...")

        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()