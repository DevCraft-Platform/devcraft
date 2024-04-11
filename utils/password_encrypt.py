import bcrypt
import sys
import secrets

def encrypt_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def check_password(password: str, encrypted_password: str) -> bool:
    return bcrypt.checkpw(password.encode(), encrypted_password)

def reset_password():
    new_password = secrets.token_urlsafe(16)
    encrypt_password = encrypt_password(new_password)
    print(f"New Password: {new_password}")
    print(f"Encrypted Password: {encrypt_password}")

def main():
    password = sys.argv[1]
    if "--encrypt" in sys.argv:
        encrypted_password = encrypt_password(password)
        print(f"Encrypted Password: {encrypted_password}")
    elif "--check" in sys.argv:
        encrypted_password = sys.argv[2]
        is_valid = check_password(password, encrypted_password)
        print(f"Is Valid: {is_valid}")
    elif "--reset" in sys.argv:
        reset_password()
    

if __name__ == "__main__":
    main()