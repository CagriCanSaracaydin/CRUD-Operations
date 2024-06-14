# main.py
from crud_operations import *

def main():
    print("Initial Users and Accounts:")
    fetch_users()
    fetch_accounts()

    # Create new user and account
    print("\nCreating new user Elif Yilmaz and her account...")
    create_user(11, 'Elif Yilmaz', 'Female', 'elif.yilmaz', 'elifpass', 'TRY')
    create_account(11, 'Elif Savings', 'Savings', 5000.00, 11)

    print("\nUsers and Accounts after adding Elif Yilmaz:")
    fetch_users()
    fetch_accounts()

    # Update user and account
    print("\nUpdating Elif Yilmaz's currency and her account balance...")
    update_user_currency(11, 'USD')
    update_account_balance(11, 5500.00)

    print("\nUser and Accounts after updates:")
    fetch_user_by_id(11)
    fetch_account_by_id(11)

    # Delete user and account
    print("\nDeleting Elif Yilmaz and her account...")
    delete_account(11)
    delete_user(11)

    print("\nFinal Users and Accounts:")
    fetch_users()
    fetch_accounts()

if __name__ == "__main__":
    main()
