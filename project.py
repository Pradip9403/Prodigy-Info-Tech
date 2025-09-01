# Caesar Cipher Project

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():
    print("=== Caesar Cipher Implementation ===")
    choice = input("Type 'E' to Encrypt or 'D' to Decrypt: ").upper()

    message = input("Enter your message: ")
    shift = int(input("Enter shift value (1-25): "))

    if choice == 'E':
        encrypted_text = caesar_encrypt(message, shift)
        print(f"Encrypted Text: {encrypted_text}")
    elif choice == 'D':
        decrypted_text = caesar_decrypt(message, shift)
        print(f"Decrypted Text: {decrypted_text}")
    else:
        print("Invalid choice! Please enter 'E' or 'D'.")

if __name__ == "__main__":
    main()