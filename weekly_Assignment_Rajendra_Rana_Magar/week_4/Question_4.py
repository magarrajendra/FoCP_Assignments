def remove_last_character(input_string):
    """
    Remove the last character from the input string.
    If the string has one or fewer characters, return it unchanged.
    :param input_string: str, the input string
    :return: str, the modified string
    """
    if len(input_string) <= 2:
        return input_string
    else:
        return input_string[:-1]


msg_1 = "Mr. John Wick.\n"
msg_2 = "Mr. John Wick."
msg_3 = "No"
modified_msg_1 = remove_last_character(msg_1)
modified_msg_2 = remove_last_character(msg_2)
modified_msg_3 = remove_last_character(msg_3)

print(f"Original text:{msg_1}Modified text:{modified_msg_1}\n\n"
      f"Original text:{msg_2}\nModified text:{modified_msg_2}\n\n"
      f"Original text:{msg_3}\nModified text:{modified_msg_3}")


