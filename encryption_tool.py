from cryptography.fernet import Fernet
import os
import time

KEY_FILE = "secret.key"

# Generate Key
def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)
    print("✓ Secret key generated successfully!")

# Load Key
def load_key():
    if not os.path.exists(KEY_FILE):
        generate_key()

    with open(KEY_FILE, "rb") as f:
        return f.read()

# Encrypt Text
def encrypt_text():
    text = input("Enter text to encrypt: ")

    key = load_key()
    cipher = Fernet(key)

    start = time.time()
    encrypted = cipher.encrypt(text.encode())
    end = time.time()

    with open("encrypted_text.txt", "wb") as f:
        f.write(encrypted)

    print("\nEncrypted Text:")
    print(encrypted.decode())
    print(f"Encryption Time: {end-start:.6f} seconds")

# Decrypt Saved Text File
def decrypt_text():
    try:
        with open("encrypted_text.txt", "rb") as f:
            encrypted = f.read()

        key = load_key()
        cipher = Fernet(key)

        start = time.time()
        decrypted = cipher.decrypt(encrypted)
        end = time.time()

        print("\nDecrypted Text:")
        print(decrypted.decode())
        print(f"Decryption Time: {end-start:.6f} seconds")

    except Exception as e:
        print("Error:", e)

# NEW FEATURE: Decrypt Pasted Text
def decrypt_pasted_text():
    try:
        encrypted_text = input("Paste encrypted text: ")

        key = load_key()
        cipher = Fernet(key)

        start = time.time()
        decrypted = cipher.decrypt(encrypted_text.encode())
        end = time.time()

        print("\nDecrypted Text:")
        print(decrypted.decode())
        print(f"Decryption Time: {end-start:.6f} seconds")

    except Exception:
        print("Invalid encrypted text or wrong key!")

# Encrypt File
def encrypt_file():
    file_name = input("Enter file name: ")

    try:
        with open(file_name, "rb") as file:
            data = file.read()

        key = load_key()
        cipher = Fernet(key)

        encrypted_data = cipher.encrypt(data)

        with open(file_name + ".enc", "wb") as file:
            file.write(encrypted_data)

        print("✓ File encrypted successfully!")
        print("Encrypted File:", file_name + ".enc")

    except FileNotFoundError:
        print("File not found!")

# Decrypt File
def decrypt_file():
    file_name = input("Enter encrypted file name: ")

    try:
        with open(file_name, "rb") as file:
            encrypted_data = file.read()

        key = load_key()
        cipher = Fernet(key)

        decrypted_data = cipher.decrypt(encrypted_data)

        output_file = "decrypted_" + file_name.replace(".enc", "")

        with open(output_file, "wb") as file:
            file.write(decrypted_data)

        print("✓ File decrypted successfully!")
        print("Saved as:", output_file)

    except Exception:
        print("Invalid encrypted file or wrong key!")

# Main Menu
while True:
    print("\n")
    print("===================================")
    print(" DATA ENCRYPTION & DECRYPTION TOOL ")
    print("===================================")
    print("1. Generate Key")
    print("2. Encrypt Text")
    print("3. Decrypt Saved Text")
    print("4. Encrypt File")
    print("5. Decrypt File")
    print("6. Decrypt Pasted Text")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        generate_key()

    elif choice == "2":
        encrypt_text()

    elif choice == "3":
        decrypt_text()

    elif choice == "4":
        encrypt_file()

    elif choice == "5":
        decrypt_file()

    elif choice == "6":
        decrypt_pasted_text()

    elif choice == "7":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")