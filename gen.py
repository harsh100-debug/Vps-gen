import random
import string
import secrets
import time
import os
from faker import Faker

class AccountGenerator:
    def __init__(self):
        self.fake = Faker()

    def generate_default_email(self, domains):
        domain = random.choice(domains)
        username = self.fake.user_name()
        return f"{username}@{domain}"

    def generate_email_with_numbers(self, domains):
        domain = random.choice(domains)
        username = self.fake.user_name() + ''.join(str(random.randint(0, 9)) for _ in range(3))
        return f"{username}@{domain}"

    def generate_email_with_special_chars(self, domains):
        domain = random.choice(domains)
        username = self.fake.user_name() + ''.join(random.choice(string.punctuation) for _ in range(3))
        return f"{username}@{domain}"

    def generate_random_password(self, length=10):
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(secrets.choice(characters) for _ in range(length))

    def generate_username_password(self, username):
        return username

    def generate_numbers_password(self, length=6):
        return ''.join(str(random.randint(0, 9)) for _ in range(length))

    def generate_random_string_password(self, length=8):
        characters = string.ascii_letters + string.digits
        return ''.join(secrets.choice(characters) for _ in range(length))

    def generate_accounts_with_passwords(self, num_accounts):
        default_domains = ['gmail.com', 'hotmail.com', 'outlook.com']
        accounts_with_passwords = []
        for _ in range(num_accounts):
            rand = random.random()
            if rand < 0.2:
                email = self.generate_email_with_special_chars(default_domains)
            elif rand < 0.4:
                email = self.generate_email_with_numbers(default_domains)
            else:
                email = self.generate_default_email(default_domains)
            password_type = random.randint(1, 4)
            if password_type == 1:
                password = self.generate_random_password()
            elif password_type == 2:
                password = self.generate_username_password(email.split('@')[0])
            elif password_type == 3:
                password = self.generate_numbers_password()
            else:
                password = self.generate_random_string_password()
            accounts_with_passwords.append({"email": email, "password": password})
        return accounts_with_passwords

    def save_accounts_to_file(self, accounts, filename='accounts.txt'):
        with open(filename, "w") as file:
            for account in accounts:
                file.write(f"{account['email']}:{account['password']}\n")

    def generate_and_save_accounts(self, num_accounts, filename='accounts.txt'):
        start_time = time.time()
        try:
            accounts_with_passwords = self.generate_accounts_with_passwords(num_accounts)
            self.save_accounts_to_file(accounts_with_passwords, filename)
            print(f"{num_accounts} accounts with passwords generated and saved to '{filename}'.")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            end_time = time.time()
            print(f"Execution time: {end_time - start_time:.2f} seconds")
            print("SUBSCRIBE TO Thunder Legend YT")
            print("Made by Thunder Legend YT")

if __name__ == "__main__":
    try:
        num_accounts = int(input("Enter the number of accounts to generate: "))
        generator = AccountGenerator()
        generator.generate_and_save_accounts(num_accounts)
    except ValueError:
        print("Please enter a valid number of accounts.")