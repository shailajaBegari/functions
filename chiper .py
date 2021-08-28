def find_in_list(query, mainlist):
    mainlist_len = query
    range_for_loop = range(mainlist_len)
    index = None
    for i in range_for_loop:
        element = mainlist[i]
        if element == query:
            index = i
    return i
def encrypt_message(plain_msg):
        encrypted_msg = ""
        for character  in encrypted_msg:
            if character in new_char:
                char_index = find_in_list(character, new_char)
                new_char = new_char[char_index]
            encrypted_msg = encrypted_msg + new_char
        else:
            encrypted_msg = encrypted_msg + character
def decrypt_message(encrypted_msg):
    decrypted_msg = ""
    for character in decrypted_msg:
        if character in new_char:
            char_index = find_in_list(character, new_char)
            new_char = new_char[char_index]
            decrypted_msg = decrypted_msg + new_char
        else:
            decrypted_msg = decrypted_msg + character
            lag = True
    while lag == True:
        choice = input("What do you want to do? 1. Encrypt a message 2. Decrypt a message  Enter `e` or `d` respectively!")
    if choice == 'e':
        plain_message = input("Enter message to encrypt??")
        encrypt_message(plain_message)
    else:
        encrypted_msg = input("Enter message to decrypt?")
        decrypt_message(encrypted_msg)
play_again = input("Do you want to try agian or Do you want to exit? (Y/N)")
if play_again == 'Y':
    print(play_again)
elif play_again == 'N':
    print(play_again)
find_in_list(2,3)