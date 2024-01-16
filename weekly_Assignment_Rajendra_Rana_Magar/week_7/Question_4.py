def letter_frequency(msg):
    msg = msg.lower()

    letter_counts = {char: 0 for char in "abcdefghijklmnopqrstuvwxyz"}

    for char in msg:
        if char.isalpha():
            letter_counts[char] += 1

    most_common_letters = sorted(letter_counts, key=letter_counts.get, reverse=True)[:6]

    print("Six most common letters and their counts:")
    for char in most_common_letters:
        count = letter_counts[char]
        print(f"{char}: {count}")


if __name__ == "__main__":
    message = "Martinez, Mr John Wick is here and he has brought a surprise gift for you!"
    letter_frequency(message)
