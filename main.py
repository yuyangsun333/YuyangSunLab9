# Yuyang Sun
# UFID: 38133550

def encode_password(password):
    encoded = ""
    for digit in password:
        new_digit = (int(digit) + 3) % 10
        encoded += str(new_digit)
    return encoded


def main():
    last_encoded_password = None
    while True:
        print("\nMenu\n-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = input("Please enter an option: ")

        if option == '1':
            password = input("Please enter your password to encode: ")
            if len(password) == 8 and password.isdigit():
                last_encoded_password = encode_password(password)
                print("Your password has been encoded and stored!")
            else:
                print("Invalid input. Please enter exactly 8 digits.")

        elif option == '2':
            if last_encoded_password:
                original_password = decode_password(last_encoded_password)
                print(f"The encoded password is {last_encoded_password}, and the original password is {original_password}.")
            else:
                print("No password has been encoded yet. Please encode a password first.")

        elif option == '3':
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()