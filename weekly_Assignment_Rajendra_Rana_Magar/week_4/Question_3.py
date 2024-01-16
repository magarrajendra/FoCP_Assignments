get_name = input("Hello, What is your name? ")

if get_name:
    formatted_name = get_name.title()
    print(f"Hello, {formatted_name}. Good to meet you!")
else:
    print(f"Hello, Stranger!")
