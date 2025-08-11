def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    # Adjust shift for decryption
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - start + shift) % 26 + start)
            result += new_char
        else:
            result += char  # Keep non-alphabet characters unchanged
    
    return result

def main():
    print("=== Caesar Cipher Tool ===")
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value (1-25): "))
    
    encrypted = caesar_cipher(message, shift, 'encrypt')
    decrypted = caesar_cipher(encrypted, shift, 'decrypt')
    
    print(f"Original : {message}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")

if __name__ == "__main__":  # <-- Correct main function check
    main()
