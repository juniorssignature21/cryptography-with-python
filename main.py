from modules.hash import hash_file, verify_integrity
from modules.encryption import aes_ed, rsa_ed
from modules.password import check_password, hash_pw, verify_password
from getpass import getpass
import time


def menu():
    print("\n\nLoading...")
    time.sleep(2)
    print("\n\nSelect an option:")
    print("1. Hash a file")
    print("2. Verify file integrity")
    print("3. AES Encrypt/Decrypt")
    print("4. RSA Encrypt/Decrypt")
    print("5. Password manager")
    print("0. Exit")
    
print("""
      Initializing Cryptography with Python Application
      ------------------------------------------------------
        \nWelcome, Agent Cipher! Choose your operation wisely.
        - Analyze and hash files to ensure integrity.
        - Encrypt and decrypt sensitive data using AES and RSA.
        - Securely hash and verify passwords.
      ------------------------------------------------------
      All systems are operational. Proceed with caution!
      """)

while True:
    menu()
    choice = input("Enter choice(0-5): ")
    if choice == "0":
        break
    elif choice == "1":
        file_path = input("Enter file path: ")
        print("\nSHA hash file is: ", hash_file(file_path))
    elif choice == "2":
        file_path1 =  input("Enter file path 1: ")
        file_path2 =  input("Enter file path 2: ")
        print(verify_integrity(file_path1, file_path2))
    elif choice == "3":
        message = input("Enter message: ")
        key, ciphertext, plaintext = aes_ed(message)
        print("AES Key: ", key)
        print("AES ciphertext: ", ciphertext)
        print("AES plaintext: ", plaintext)
    elif choice == "4":
        message = input("Enter a message: ")
        ciphertext, plaintext = rsa_ed(message)
        print("RSA message, encrypted with a public key: ", ciphertext)
        print("RSA message, decrypted with a private key: ", plaintext)
        
    elif choice == "5":
        while True:
            password1 =getpass("Enter a Password to check strength: ")
            print(check_password(password1))
            if check_password(password1).startswith("Weak"):
                print("Please choose a stronger password")
            else:
                break 
        
        hashed_pw = hash_pw(password1)
        print(f"Hashed Password: {hashed_pw}")
        pw_attempt = getpass("Re-enter your password for verification: ")
        print(verify_password(pw_attempt, hashed_pw))
    else:
        print("Invalid Choice.")
print("Agent, You are exiting your crytography toolkit. Stay sharp and secure out there.")