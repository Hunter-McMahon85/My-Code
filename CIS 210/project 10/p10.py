"""
Hunter McMahon
CIS 210
Project 10
Desc: the final project
"""
import turtle


# TODO: write your functions here, make sure to match required prototypes
# Don't forget to include doctests as required

def count_smaller(lst: list, item: int) -> int:
    """
    Counts the number of items in a list that are smaller than some value.
    You can assume the list is sorted in ascending order.
    Args:
        lst: list to be searched
        item: item to be searched for
    Returns:
        number of items smaller than item
    def count_smaller(lst: list, item: int) -> int:
    Counts the number of items in a list that are smaller than some value.
    You can assume the list is sorted in ascending order.
    Args:
        lst: list to be searched
        item: item to be searched for
    Returns:
        number of items smaller than item
    >>> count_smaller([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
    4
    >>> count_smaller([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)
    0
    >>> count_smaller([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6)
    5
    """
    if item in lst:
        if lst[0] == item:
            return 0
        else:
            return 1 + count_smaller(lst[1:], item)
    else:
        return 0


def is_palindrome(s: str) -> bool:
    """
    Recursively checks if a string is a palindrome.
    Args:
        s: string to be checked
    Returns:
        True if string is a palindrome, False otherwise
    >>> is_palindrome('racecar')
    True
    >>> is_palindrome('racecars')
    False
    """
    if len(s) < 2:
        return True
    elif s[0] == s[len(s) - 1]:
        return is_palindrome(s[1: len(s) - 1])
    else:
        return False


def avg_word_length(lst: list, length: int = 0, count: int = 0) -> float:
    """
    Recursively finds the average word length in a list of words.
    Args:
        lst: list of words
    Returns:
        average word length
    >>> avg_word_length(['hello', 'world'])
    5.0
    >>> avg_word_length(['hello', 'world', 'meh'])
    4.3
    """
    # TODO: write your code here
    if len(lst) == 1:
        return len(lst[0])
    else:
        list_len = len(lst)
        return round((len(lst[0]) + (list_len - 1) * avg_word_length(lst[1:])) / list_len, 1)


def draw_tree(the_turtle: turtle.Turtle, length: int) -> None:
    """
    Draws a tree using recursion and the turtle module.
    Args:
        turtle: turtle object
        length: length of the branch/trunk
    Returns:
        None
    """
    # TODO: write your code here
    pass


# Generate points Sierpinski triangle using recursion
def sierpinski(the_turtle: turtle.Turtle, points: tuple, degree: int) -> list:
    """
    Generates the points for a Sierpinski triangle using recursion, returning a list of points.
    Args:
        the_turtle: turtle object
        points: tuple of 2-d points (tuples) of initial triangle
        degree: degree of the Sierpinski triangle
    Returns:
        list of all points for the Sierpinski triangle
    """
    # TODO: write your code here
    pass


# ---- You shouldn't have to change anything below this line
# ---- unless you implemented the optional problems 10.4 and 10.5

def save_png(the_turtle: turtle.Turtle, filename: str) -> None:
    """
    Saves the current image of the turtle as a PNG file.
    Args:
        the_turtle: turtle object
        filename: name of the file to be saved
    Returns:
        None
    """
    from PIL import Image
    import io
    if the_turtle.screen.getcanvas() is not None:
        ps = the_turtle.getscreen().getcanvas().postscript(colormode='color')
        img = Image.open(io.BytesIO(ps.encode('utf-8')))
        try:
            img.save(filename, 'png')
            print(f"Saved image to {filename}")
        except Exception as e:
            print(f"Error: Could not save image in {filename} file: {e}")
    return


def main():
    # Part 10.1
    print('Part 10.1')
    print('Counting smaller items in a list')
    print('5 in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] is', count_smaller([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))

    # Part 10.2
    print('\nPart 10.2')
    print('Recursively check if a string is a palindrome')
    print('racecar is a palindrome:', is_palindrome('racecar'))
    print('racecars is a palindrome:', is_palindrome('racecars'))

    # Part 10.3
    print('\nPart 10.3')
    print('Average word length in a list of words')
    wordlist = ['not', 'a', 'very', 'long', 'word', 'list']
    print(f'avg word length of {wordlist} is', avg_word_length(wordlist))

    # Part 10.4
    if False:  # change to True if you implement the optional part 10.4
        print('\nOPTIONAL Part 10.4')
        print('Drawing a tree using recursion and the turtle module')
        yurtle = turtle.Turtle()
        yurtle.penup()
        yurtle.setpos(0, -250)  # move closer to bottom of canvas
        yurtle.pendown()
        yurtle.speed(0)
        yurtle.left(90)  # Tree will grow upwards
        draw_tree(yurtle, 120)
        save_png(yurtle, 'tree.png')

        # Part 10.5
    if False:  # Change to True if you implement the optional 10.5
        print('\nOPTIONAL Part 10.5')
        print('Generating points for a Sierpinski triangle using recursion')
        yurtle = turtle.Turtle()
        yurtle.speed(0)
        sierpinski(yurtle, points=((-100, -50), (0, 100), (100, -50)), degree=3):
        save_png(yurtle, 'sierpinski.png')


if __name__ == '__main__':
    main()