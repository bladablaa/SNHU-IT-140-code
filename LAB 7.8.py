import csv


def word_frequency(file_name):
    word_count = {}

    with open('file_name', 'r') as file:
        reader = csv.reader(file)

        for row in reader:
            for word in row:
                word = word.strip().lower()

                word_count = word_count.get(word, 0) + 1

    return word_count


def main():
    # Read the name of the input file
    file_name = input()

    # Calculate word frequencies
    frequencies = word_frequency(file_name)

    # Output unique words and their frequencies
    for word, frequency in frequencies.items():
        print(f"{word} {frequency}")


if __name__ == "__main__":
    main()