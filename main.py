from all_neos import all_neos
from large_neos import show_large_neos

def main_menu():
    neos = all_neos()  # fetch once and get the list

    while True:
        print("Welcome to NASA Near Earth Objects (NEO) explorer! 🚀")
        choice = input("""
        Please choose one of the following options below to continue:
                       
        1️⃣. List all NEOs from the last 4 weeks
        2️⃣. Show potentially hazardous NEOs
        3️⃣. Show large NEOs (>50m)
        4️⃣. Exit
        """).strip()

        if choice == "1":
            print("Listing all NEOs from the last 4 weeks...")
            for i in range(0, len(neos), 10):
                from tabulate import tabulate
                print(tabulate(neos[i:i+10], headers="keys", tablefmt="fancy_grid"))
                if i + 10 < len(neos):
                    input("Press Enter to continue...")

        elif choice == "2":
            print("Showing potentially hazardous NEOs...")
            hazardous = [n for n in neos if n["Hazardous"] == "Yes"]
            from tabulate import tabulate
            for i in range(0, len(hazardous), 10):
                print(tabulate(hazardous[i:i+10], headers="keys", tablefmt="fancy_grid"))
                if i + 10 < len(hazardous):
                    input("Press Enter to continue...")

        elif choice == "3": 
            print("Showing large NEOs (>50m)...")
            show_large_neos(neos)
            input("\nPress Enter to return to the main menu...")

        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()

from all_neos import all_neos

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
            input("\nPress Enter to return to the main menu...")

        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()