# Author: Mayank Kumar Pokhriyal
# Date: 14th March 2025
# Description: This script performs term frequency analysis on a text file while excluding stopwords.
#              It reads stopwords from a specified file and outputs the top 10 most frequent words.
import os
import string


def readStopWordsFile(stop_set):
    """Reads stopwords from a file into the provided set."""
    while True:
        filename = input("Enter the stopwords filename: ")
        if os.path.exists(filename):
            break
        print(f"{filename} does not exist! Please enter the name of the stopwords file:", end=" ")
    with open(filename, 'r') as file:
        for line in file:
            word = line.strip().lower()
            if word:
                stop_set.add(word)


def readTextFile(word_dict, stop_set):
    """Reads a text file and populates the dictionary with word frequencies, excluding stopwords."""
    while True:
        filename = input("Please enter the name of the file to analyze: ")
        if os.path.exists(filename):
            break
        print(f"{filename} does not exist! Please enter the name of the file to analyze:", end=" ")
    with open(filename, 'r') as file:
        text = file.read().lower()
    words = text.split()
    for word in words:
        processed_word = word.strip(string.punctuation)
        if processed_word and processed_word not in stop_set:
            word_dict[processed_word] = word_dict.get(processed_word, 0) + 1


def main():
    word_freq = {}
    stop_words = set()
    readStopWordsFile(stop_words)
    readTextFile(word_freq, stop_words)
    sorted_words = sorted(word_freq.items(), key=lambda x: (-x[1], x[0]))

    print(f"\nThe file contained {len(sorted_words)} unique words.")
    for word, count in sorted_words:  # Removed top 10 slicing
        print(f"{word}:{count}")


if __name__ == "__main__":
    main()