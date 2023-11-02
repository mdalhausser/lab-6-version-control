# Max Dalhausser

def encoding(dec_password):
    password = 0
    new_list = list(dec_password)
    dec_password = 0
    for i in new_list:
        new_list[password] = int(i) + 3
        if new_list[password] == 10:
            new_list[password] = "0"
        elif new_list[password] == 11:
            new_list[password] = "1"
        elif new_list[password] == 12:
            new_list[password] = "2"
        password += 1
    password = 0
    for i in new_list:
        new_list[password] = str(i)
        password += 1
    return "".join(new_list)


def main():
    user_input = 0
    enc_password = 0
    dec_password = 0
    result = 0
    while user_input != 3:
        print("Menu\n------------")
        print("1. Encode\n2. Decode\n3. Quit")
        user_input = int(input("Please enter an option: "))
        if user_input == 3:
            break
        if user_input == 1:
            dec_password = input("Please enter your password to encode: ")
            result = encoding(dec_password)
            print("Your password has been encoded and stored!")
        if user_input == 2:
            enc_password = result
            result = decoding(enc_password)
            print(f"The encoded password is {enc_password}, and the original password is {dec_password}.")


if __name__ == "__main__":
    main()