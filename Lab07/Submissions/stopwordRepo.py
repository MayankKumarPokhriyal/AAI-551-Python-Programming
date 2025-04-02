# Author: Mayank Kumar Pokhriyal
# Date: 14th March 2025
# Description: Repository for managing stopwords with automatic duplicate removal using pickling.

import os
import pickle

PICKLE_FILE = "stopwordset.data"


def readStopWordsFile(stopwords):
    while True:
        filename = input("Please enter the name of the new stopwords file: ")
        if os.path.exists(filename):
            break
        print(f"File '{filename}' does not exist. Please try again.")

    with open(filename, 'r') as file:
        for line in file:
            word = line.strip()
            if word in stopwords:
                print(f"We already have the word: {word}")
            else:
                stopwords.add(word)


def writeStopWordsFile(stopwords):
    filename = input("Please enter the name of the stopwords file to write to: ")
    with open(filename, 'w') as file:
        for word in sorted(stopwords):
            file.write(word + '\n')


def displayStopWords(stopwords):
    print(f"Currently we have {len(stopwords)} stopwords:")
    for word in sorted(stopwords):
        print(word)


def storeStopWords(stopwords):
    with open(PICKLE_FILE, 'wb') as file:
        pickle.dump(stopwords, file)


def restoreStopWords():
    if os.path.exists(PICKLE_FILE):
        with open(PICKLE_FILE, 'rb') as file:
            return pickle.load(file)
    return set()


def main():
    stopwords = restoreStopWords()
    print("Welcome to the stopword repository!")

    while True:
        print("\nPlease choose from the following options:")
        print("1. Add a new list of stopwords")
        print("2. Write current set of stopwords to a file")
        print("3. Display current set of stopwords")
        print("4. Quit")
        choice = input("Please enter your choice: ")

        if choice == '1':
            readStopWordsFile(stopwords)
        elif choice == '2':
            writeStopWordsFile(stopwords)
        elif choice == '3':
            displayStopWords(stopwords)
        elif choice == '4':
            storeStopWords(stopwords)
            print("Thank you for using the stopword repository!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()