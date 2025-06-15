import sys
from bank_account import BankAccount
def main():
    account = BankAccount(100)
    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)
    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None
    if command == "deposit":
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw":
        if account.withdraw(amount):
            print(f"Withdraw: ${amount}")
        else:
            print("Insufficient balance")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command")
if __name__ == "__main__":
    main()