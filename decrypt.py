from cryptography.fernet import Fernet

def load_key():
    """Loads the key from the current directory."""
    return open("thekey.key", "rb").read()

def decrypt_file(file_path, key):
    """Decrypts a single file."""
    f = Fernet(key)
    with open(file_path, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()

    decrypted_data = f.decrypt(encrypted_data)

    with open(file_path, "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)
    print(f"Decrypted: {file_path}")

# main
if __name__ == "__main__":
    KEY = load_key()
    TARGET_DIRECTORY = "/path/to/your/test_directory"

    for root, _, files in os.walk(TARGET_DIRECTORY):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                decrypt_file(file_path, KEY)
    print("\nDecryption complete.")
