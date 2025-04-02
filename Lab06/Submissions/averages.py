# Author: Mayank Kumar Pokhriyal
# Date: 6th March 2025
# Description: Reads integers from numbers.txt, computes their average, and prints the result.


def main():
    # Open the file for reading
    with open('numbers.txt', 'r') as file:
        total = 0  # Initialize variable to keep track of the total sum
        count = 0  # Initialize variable to count the number of lines

        # Read each line in the file
        for line in file:
            # Remove any newlines or extra spaces from the line
            line = line.strip()

            # Print the current line
            print(line)

            # Convert the line to an integer and add it to the total
            total += int(line)

            # Increment the count
            count += 1

        # Compute the average
        if count > 0:
            average = total / count
            print(f"The average of the numbers is {average}")
        else:
            print("No numbers to calculate the average.")

# Call the main function
if __name__ == "__main__":
    main()