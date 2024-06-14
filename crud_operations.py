# crud_operations.py
import mysql.connector
from mysql.connector import Error
from db_connection import db_connect

def print_users():
    print("\nCurrent Users:")
    fetch_users()

def print_accounts():
    print("\nCurrent Accounts:")
    fetch_accounts()

def create_user(user_id, name, gender, username, password, currency):
    if not isinstance(user_id, int) or not isinstance(name, str) or not isinstance(gender, str) or \
            not isinstance(username, str) or not isinstance(password, str) or not isinstance(currency, str):
        raise TypeError("Invalid input types provided")

    query = "INSERT INTO User (UserID, Name, Gender, Username, Password, Currency) VALUES (%s, %s, %s, %s, %s, %s)"
    conn = db_connect()
    if conn:
        try:
            print("Before Create User:")
            print_users()
            cursor = conn.cursor()
            print("Executing query:", query % (user_id, name, gender, username, password, currency))
            cursor.execute(query, (user_id, name, gender, username, password, currency))
            conn.commit()
            print("User created successfully.")
            print("After Create User:")
            print_users()
        except Error as e:
            print(f"Error while creating user: {e}")
        finally:
            conn.close()

def create_account(account_id, account_name, account_type, balance, user_id):
    if not all([account_id, account_name, account_type, balance, user_id]):
        print("Invalid input data. Please check your values.")
        return

    query = "INSERT INTO Account (AccountID, AccountName, Type, Balance, UserID) VALUES (%s, %s, %s, %s, %s)"
    conn = db_connect()
    if conn:
        try:
            print("Before Create Account:")
            print_accounts()
            cursor = conn.cursor()
            print("Executing query:", query % (account_id, account_name, account_type, balance, user_id))
            cursor.execute(query, (account_id, account_name, account_type, balance, user_id))
            conn.commit()
            print("Account created successfully.")
            print("After Create Account:")
            print_accounts()
        except Error as e:
            print(f"Error while creating account: {e}")
        finally:
            conn.close()

def fetch_user_by_id(user_id):
    query = "SELECT * FROM User WHERE UserID = %s"
    conn = db_connect()
    if conn:
        try:
            cursor = conn.cursor()
            print("Executing query:", query % user_id)
            cursor.execute(query, (user_id,))
            result = cursor.fetchone()
            if result:
                print(result)
            else:
                print(f"No user found with UserID {user_id}")
        except Error as e:
            print(f"Error fetching user: {e}")
        finally:
            conn.close()

def fetch_users():
    query = "SELECT * FROM User LIMIT 20"
    conn = db_connect()
    if conn:
        try:
            cursor = conn.cursor()
            print("Executing query:", query)
            cursor.execute(query)
            results = cursor.fetchall()
            for result in results:
                print(result)
        except Error as e:
            print(f"Error fetching users: {e}")
        finally:
            conn.close()

def fetch_account_by_id(account_id):
    query = "SELECT * FROM Account WHERE AccountID = %s"
    conn = db_connect()
    if conn:
        try:
            cursor = conn.cursor()
            print("Executing query:", query % account_id)
            cursor.execute(query, (account_id,))
            result = cursor.fetchone()
            if result:
                print(result)
            else:
                print(f"No account found with AccountID {account_id}")
        except Error as e:
            print(f"Error fetching account: {e}")
        finally:
            conn.close()

def fetch_accounts():
    query = "SELECT * FROM Account LIMIT 20"
    conn = db_connect()
    if conn:
        try:
            cursor = conn.cursor()
            print("Executing query:", query)
            cursor.execute(query)
            results = cursor.fetchall()
            for result in results:
                print(result)
        except Error as e:
            print(f"Error fetching accounts: {e}")
        finally:
            conn.close()

def update_user_currency(user_id, new_currency):
    query = "UPDATE User SET Currency = %s WHERE UserID = %s"
    conn = db_connect()
    if conn:
        try:
            print("Before Update User Currency:")
            print_users()
            cursor = conn.cursor()
            print("Executing query:", query % (new_currency, user_id))
            cursor.execute(query, (new_currency, user_id))
            conn.commit()
            if cursor.rowcount > 0:
                print("User currency updated successfully.")
            else:
                print("No user was updated. Check if the UserID exists.")
            print("After Update User Currency:")
            print_users()
        except Error as e:
            print(f"Error updating user currency: {e}")
        finally:
            conn.close()

def update_account_balance(account_id, new_balance):
    query = "UPDATE Account SET Balance = %s WHERE AccountID = %s"
    conn = db_connect()
    if conn:
        try:
            print("Before Update Account Balance:")
            print_accounts()
            cursor = conn.cursor()
            print("Executing query:", query % (new_balance, account_id))
            cursor.execute(query, (new_balance, account_id))
            conn.commit()
            if cursor.rowcount > 0:
                print("Account balance updated successfully.")
            else:
                print("No account was updated. Check if the AccountID exists.")
            print("After Update Account Balance:")
            print_accounts()
        except Error as e:
            print(f"Error updating account balance: {e}")
        finally:
            conn.close()

def delete_user(user_id):
    query = "DELETE FROM User WHERE UserID = %s"
    conn = db_connect()
    if conn:
        try:
            print("Before Delete User:")
            print_users()
            cursor = conn.cursor()
            print("Executing query:", query % user_id)
            cursor.execute(query, (user_id,))
            conn.commit()
            if cursor.rowcount > 0:
                print("User deleted successfully.")
            else:
                print("No user was deleted. Check if the UserID exists.")
            print("After Delete User:")
            print_users()
        except Error as e:
            print(f"Error deleting user: {e}")
        finally:
            conn.close()

def delete_account(account_id):
    query = "DELETE FROM Account WHERE AccountID = %s"
    conn = db_connect()
    if conn:
        try:
            print("Before Delete Account:")
            print_accounts()
            cursor = conn.cursor()
            print("Executing query:", query % account_id)
            cursor.execute(query, (account_id,))
            conn.commit()
            if cursor.rowcount > 0:
                print("Account deleted successfully.")
            else:
                print("No account was deleted. Check if the AccountID exists.")
            print("After Delete Account:")
            print_accounts()
        except Error as e:
            print(f"Error deleting account: {e}")
        finally:
            conn.close()
