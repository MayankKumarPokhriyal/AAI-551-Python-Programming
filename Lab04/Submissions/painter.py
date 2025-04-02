# Author: Mayank Kumar Pokhriyal
# Date: 21st Feb 2025
# Description: ASCII Art Printer with Customizable Borders

def intro():
    """
    Welcomes user and collects their art/border preferences.
    Returns:
        tuple: (user_choice (int), border_symbol (str))
    """
    print("Welcome to the painting printer!")
    print("   We have many options:")
    print("   1. The S.S. Satisfaction")
    print("   2. Mina in Repose")
    print("   3. The Fish")
    print("   4. Funny Rabbit")
    choice = int(input("Please select a painting to print: "))
    border = input("What border would you like around your painting: ")
    return choice, border


def printHeaderFooter(border, size):
    """
    Prints top/bottom borders for the artwork
    Args:
        border (str): Border character
        size (int): Length of border line
    """
    print(border * size)


def sleepingCat(border):
    """Displays sleeping cat ASCII art with borders"""
    art = [
        r"      |\\      _,,,---,,_     ",
        r"ZZZzz /,`.-'`'    -.  ;-;;,_  ",
        r"     |,4-  ) )-,_. ,\\ (  `'-'",
        r"    '---''(_/--'  `-'\\_)     "

    ]
    max_width = max(len(line) for line in art)
    printHeaderFooter(border, max_width + 2)
    for line in art:
        print(f"{border}{line.center(max_width)}{border}")
    printHeaderFooter(border, max_width + 2)


def sailingShip(border):
    """Displays sailing ship ASCII art with borders"""
    art = [
        r"      |    |    |            ",
        r"     )_)  )_)  )_)           ",
        r"    )___))___))___)\\        ",
        r"   )____)____)_____)\\\\     ",
        r" _____|____|____|____\\\\\\__",
        r"\\    Satisfaction   /       ",
        r"^^^^^^^^^^^^^^^^^^^^^^^^^^^^ "
    ]
    max_width = max(len(line) for line in art)
    printHeaderFooter(border, max_width + 2)
    for line in art:
        print(f"{border}{line.ljust(max_width)}{border}")
    printHeaderFooter(border, max_width + 2)


def rabbit(border):
    """Displays oak rabbit ASCII art with borders"""
    art = [
        r"             ,\         ",
        r"             \\\,_      ",
        r"              \` ,\     ",
        r"         __,.-\" =__)    ",
        r"       .\"        )      ",
        r"    ,_/   ,    \/\_     ",
        r"    \_|    )_-\ \_-`    ",
        r"       `-----` `--`     "
    ]
    max_width = max(len(line) for line in art)
    printHeaderFooter(border, max_width + 2)
    for line in art:
        print(f"{border}{line.center(max_width)}{border}")
    printHeaderFooter(border, max_width + 2)


def fish(border):
    """Displays fish ASCII art with borders"""
    art = [
        r"      /`·.¸         ",
        r"     /¸...¸`:·      ",
        r" ¸.·´  ¸   `·.¸.·´) ",
        r": © ):´;      ¸  {  ",
        r" `·.¸ `·  ¸.·´\`·¸) ",
        r"     `\\´´\¸.·´     "
    ]
    max_width = max(len(line) for line in art)
    printHeaderFooter(border, max_width + 2)
    for line in art:
        print(f"{border}{line.ljust(max_width)}{border}")
    printHeaderFooter(border, max_width + 2)


def blank(border):
    """Displays blank canvas with borders"""
    canvas_width = 7  # 5 spaces + 2 borders
    printHeaderFooter(border, canvas_width)
    for _ in range(5):
        print(f"{border}     {border}")
    printHeaderFooter(border, canvas_width)


def main():
    """Main program controller"""
    choice, border = intro()

    if choice == 1:
        sailingShip(border)
    elif choice == 2:
        sleepingCat(border)
    elif choice == 3:
        fish(border)
    elif choice == 4:
        rabbit(border)
    else:
        blank(border)
        print("\nError: Invalid selection! Art not found.")
        exit(-1)

    print("We hope you enjoy your art!")


if __name__ == "__main__":
    main()