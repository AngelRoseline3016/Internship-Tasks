from PIL import Image

KEY = 123  # XOR encryption key (must be same for encryption and decryption)

def encrypt_image(input_path, output_path):
    """Encrypts an image by manipulating its pixels."""
    image = Image.open(input_path)
    pixels = image.load()

    for i in range(image.size[0]):  # width
        for j in range(image.size[1]):  # height
            pixel = pixels[i, j]

            if len(pixel) == 4:  # RGBA
                r, g, b, a = pixel
                r, g, b = (r ^ KEY), (g ^ KEY), (b ^ KEY)
                pixels[i, j] = (r, g, b, a)
            else:  # RGB
                r, g, b = pixel
                r, g, b = (r ^ KEY), (g ^ KEY), (b ^ KEY)
                pixels[i, j] = (r, g, b)

    image.save(output_path)
    print(f"[✔] Image saved as {output_path}")

def decrypt_image(input_path, output_path):
    """Decrypts an image (same process as encryption)."""
    encrypt_image(input_path, output_path)

if __name__ == "__main__":
    print("=== Image Encryption Tool ===")
    print("1. Encrypt Image")
    print("2. Decrypt Image")
    choice = input("Enter your choice (1/2): ").strip()

    if choice == '1':
        input_file = input("Enter the path of the image to encrypt: ").strip()
        output_file = input("Enter the output encrypted image filename: ").strip()
        encrypt_image(input_file, output_file)

    elif choice == '2':
        input_file = input("Enter the path of the encrypted image to decrypt: ").strip()
        output_file = input("Enter the output decrypted image filename: ").strip()
        decrypt_image(input_file, output_file)

    else:
        print("[!] Invalid choice. Please run again.")
