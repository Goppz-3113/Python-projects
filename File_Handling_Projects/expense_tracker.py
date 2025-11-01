#Expense Tracker

import os                                                            #module that let you works with computer's file and folders

class ExpenseTracker:                                                # creates a blueprint for all the tasks
    def __init__(self,filename="expense.txt"):                       #"expense.txt" is a default file name used if user doesnt give one
        self.filename=filename
        if not os.path.exists(self.filename):                        #checks wheather thefile exists in the computer or not
            with open(self.filename,"w") as file:                    # Opens a file in write mode and gives it a name "file", "with" automatically closes the file when we are done
                file.write("Date,Category,Amount,Descripstion\n")
    
    
    def add_expense(self,date,category,amount,description):
        with open(self.filename,"a") as file :                       # opens the file in append mode
            file.write(f"{date},{category},{amount},{description}\n")   #file.write is use to write the datas into the file
            print(f"Expense Added: {category} : ₹{amount} on {date}")

    
    def view_expense(self):
        with open(self.filename,"r") as file:                   # opens the file in read mode
            lines = file.readlines()                           # read all the lines from the file and store them in a list (here it is "lines")
        if len(lines) <=1:
            print("No Expenses Recorded Yet")
            return
        print("===All Expenses===\n")
        for line in lines[1:]:                                # skips the header by starting from line 1
            date, category, amount, description = line.strip().split(",")      #.strip() removes all extra spaces and \n and .split() splits the text whenever there is a comma
            print(f"{date} | {category} | ₹ {amount} | {description} ")

    
    def total_expenses(self):
        total=0
        with open(self.filename,"r") as file:
            next(file)   # skips the haeder
            for line in file:
                parts= line.strip().split(",")    # cuts the line into seperate pieces into a list
                if len(parts)>= 3:               # checks how many items are there in the list, making sure there are atleast 3
                    try:                          # "try" means “Try running the next line — if it causes an error, don’t crash.”
                        total +=float(parts[2])    # here part[2] means the third item on th elist which is Expense
                    except ValueError:           # If something goes wrong , this part catches the error instead of crashing. 
                        continue    # Skips to the next loop
        print(f"\n Total Expenses: ₹{total:.2f}")    # .2f is used to print the expense with 2 decimal palces


    def search_by_category(self,category):
        found= False
        with open(self.filename,"r") as file:                  #opens file in read mode
            next(file)   # skips the header
            for line in file:
                date,cat,amount,desc=line.strip().split(",")
                if cat.lower() == category.lower():          # .lower() is used here to remove case-sensitivity
                    if not found:                            # here the condition becomes True( not found(false)) so it runs the if statements
                        print(f"\n===Expenses in {category}===")
                        found=True                           # here the found turns back to true, so when it loop again the if condition become false( not found(true)), hence only printing the header once and continue loop and print the rest of the body
                    print(f"{date} | ₹{amount} | {desc}")
            if not found:                                      # If we doesnt found a match after looping the entire file, this statement get executed
                print(f"No Expenses Found In Category {category}")


def main():
    tracker=ExpenseTracker()

    while True:   
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Expenses")
        print("4. Search by Category")
        print("5. Exit")

        choice= input("Enter Your Choice(1-5): ")

        if choice == "1":
            date = input("Enter date (DD-MM-YYYY): ")
            category = input("Enter category (e.g., Food, Travel, Bills): ")
            amount = input("Enter amount: ")
            description = input("Enter short description: ")
            tracker.add_expense(date, category, amount, description)

        elif choice == "2":
            tracker.view_expenses()

        elif choice == "3":
            tracker.total_expenses()

        elif choice == "4":
            category = input("Enter category to search: ")
            tracker.search_by_category(category)

        elif choice == "5":
            print(" Exiting... !")
            break

        else:
            print(" Invalid choice. Please enter a number from 1-5.")


# The below code makes sure main() only runs when this file is executed directly,and does NOT run when this file is imported in another file.

if __name__ == "__main__":     
    main()

        




                
