# Author: Mayank Kumar Pokhriyal
# Date: 14th March 2025
# Description: This program counts the frequency of words in a text file provided by the user.
#              It processes the text by converting it to lowercase, splits it into words, and tracks
#              occurrences using a dictionary. Finally, it outputs the number of unique words and their frequencies.

import os


def readTextFile(word_counts):
    """
    Reads a text file specified by the user, processes each line to extract words, and updates their counts in a dictionary.
    Continuously prompts the user until a valid filename is provided.
    """
    filename = input("Please enter the name of the file to analyze: ")
    while not os.path.isfile(filename):
        filename = input(f"{filename} does not exist! Please enter the name of the file to analyze: ")

    with open(filename, 'r') as file:
        for line in file:
            cleaned_line = line.strip().lower()
            words = cleaned_line.split()
            for word in words:
                word_counts[word] = word_counts.get(word, 0) + 1


def outputFreq(word_counts):
    """
    Outputs the number of unique words and their frequencies in the format 'word:count'.
    """
    print(f"The file contained {len(word_counts)} unique words.")
    for word, count in word_counts.items():
        print(f"{word}:{count}")


def main():
    """
    Main function that initializes the word count dictionary, calls the file reading function, and outputs the results.
    """
    word_counts = {}
    readTextFile(word_counts)
    outputFreq(word_counts)


if __name__ == "__main__":
    main()