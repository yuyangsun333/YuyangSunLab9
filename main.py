def encode_password(password):
    encoded = ""
    for digit in password:
        new_digit = (int(digit) + 3) % 10
        encoded += str(new_digit)
    return encoded

def decode_password(encoded_password):
    decoded = ""
    for digit in encoded_password:
        new_digit = (int(digit) - 3) % 10
        decoded += str(new_digit)
    return decoded

def main():
    while True:
        print("\nPassword Encoder/Decoder Menu")
        print("1. Encode a password")
        print("2. Decode a password")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            password = input("Enter an 8-digit password to encode: ")
            if len(password) == 8 and password.isdigit():
                encoded = encode_password(password)
                print("Encoded password:", encoded)
            else:
                print("Invalid input. Please enter exactly 8 digits.")

        elif choice == '2':
            encoded_password = input("Enter an encoded password to decode: ")
            if len(encoded_password) == 8 and encoded_password.isdigit():
                decoded = decode_password(encoded_password)
                print("Decoded password:", decoded)
            else:
                print("Invalid input. Please enter exactly 8 digits.")

        elif choice == '3':
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()