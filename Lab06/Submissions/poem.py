# Author: Mayank Kumar Pokhriyal
# Date: 6th March 2025
# Description: Reads a poem file and writes a summary to Output.txt.

import os


def main():
    # Variables to store the poem's details
    title = ""
    author = ""
    poem_lines = []

    # Prompt user for the file name
    file_name = input("Please input the name of the poem you wish summarized: ")

    # Check if the file exists, and prompt until a valid file is provided
    while not os.path.exists(file_name):
        print(f"{file_name} does not exist! Please input the name of the poem you wish summarized: ")
        file_name = input()

    # Open the poem file for reading
    with open(file_name, 'r') as file:
        # Read and store the title and author from the first two lines
        title = file.readline().strip()
        author = file.readline().strip()

        # Read and store the rest of the poem lines
        poem_lines = file.readlines()

    # Open Output.txt for writing (it will create the file if it doesn't exist)
    with open("Output.txt", 'w') as output_file:
        # Write poem details to the Output.txt file
        output_file.write(f"The name of the poem is {title}\n")
        output_file.write(f"The author of the poem is {author}\n")
        output_file.write(f"The number of lines in the poem is {len(poem_lines)}\n")
        output_file.write("A preview of the poem is:\n")

        # Write the first three lines of the poem as a preview
        for i in range(min(3, len(poem_lines))):
            output_file.write(f"{poem_lines[i].strip()}\n")

    print("Summary has been written to Output.txt.")


# Run the main function
if __name__ == "__main__":
    main()