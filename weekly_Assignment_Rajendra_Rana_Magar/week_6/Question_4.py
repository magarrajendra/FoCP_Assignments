def simple_encrypt(message):
    message_without_spaces = message.replace(" ", "")

    encrypted_message = message_without_spaces[::-1]

    return encrypted_message


if __name__ == "__main__":
    original_message = "Noo, Mr. John Wick is here!!!"
    encrypted_result = simple_encrypt(original_message)
    print(f"Original Message: {original_message}")
    print(f"Encrypted Message: {encrypted_result}")
