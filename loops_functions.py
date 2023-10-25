
def atm():
    current_balance = 500000
    min = 50
    max = 5000

    while True:
        print("current balance:", current_balance)
        
        user_input = input("Do you want to withdraw money? (yes/no): ")

        if user_input == 'no':
            print("Have a nice day!")
            break

        elif user_input == 'yes':
            amount= int(input("enter the amount: "))

            if amount < min:
                print("error: amount should be at least ", min)
            elif amount > max:
                print("error: amount exceeds limit ", max)
            elif amount > current_balance:
                print("error: Insufficient funds.")
            else:
                current_balance -= amount
                print("Withdrawal successful. New balance: ", current_balance)

                another_transaction = input("want to another transaction? (yes/no): ")

                if another_transaction == 'no':
                    print("Thank you. Have a nice day!")
                    break
atm()