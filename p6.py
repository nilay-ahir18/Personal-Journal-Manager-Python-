class JournalManager:
    def __init__(self, filename="journal.txt"):
        self.filename = filename


    def add_entry(self):
        try:
            entry = input("\nEnter your journal entry:\n")

            file = open(self.filename, "a")
            file.write(entry + "\n")
            file.close()

            print("Entry added successfully!")

        except Exception as e:
            print("Error while adding entry:", e)


    def view_entries(self):
        try:
            file = open(self.filename, "r")
            content = file.read()
            file.close()

            if content.strip() == "":
                print("No journal entries found.")
            else:
                print("\nYour Journal Entries:")
                print("----------------------")
                print(content)

        except:
            print("No journal file found. Please add entries first.")

    
    def search_entry(self):
        try:
            keyword = input("\nEnter keyword to search: ").lower()
            found = False

            file = open(self.filename, "r")

            print("\nMatching Entries:")
            print("----------------------")

            for line in file:
                if keyword in line.lower():
                    print(line.strip())
                    found = True

            file.close()

            if not found:
                print("No matching entry found.")

        except:
            print("No journal file found.")


    def delete_entries(self):
        try:
            confirm = input("Are you sure you want to delete all entries? (yes/no): ").lower()

            if confirm == "yes":
                file = open(self.filename, "w")  # clears file
                file.close()
                print("All entries deleted successfully.")
            else:
                print("Deletion cancelled.")

        except Exception as e:
            print("Error while deleting:", e)



def main():
    journal = JournalManager()

    while True:
        print("\n===== Personal Journal Manager =====")
        print("1. Add Entry")
        print("2. View Entries")
        print("3. Search Entry")
        print("4. Delete All Entries")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                journal.add_entry()

            elif choice == 2:
                journal.view_entries()

            elif choice == 3:
                journal.search_entry()

            elif choice == 4:
                journal.delete_entries()

            elif choice == 5:
                print("Thank you! Goodbye.")
                break

            else:
                print("Invalid choice. Please select 1 to 5.")

        except ValueError:
            print("Invalid input! Please enter a number.")



if __name__ == "__main__":
    main()
