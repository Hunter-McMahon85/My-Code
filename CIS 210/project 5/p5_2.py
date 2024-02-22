"""
Hunter McMahon
CIS 210
p5 pt 2
description: 5-7-5
"""
from random import randint
from p5_2_words import word_dict


def first_line() -> str:
    """
    makes the first line of the poem by taking random adjectives and nouns from p5_2words.py
    Returns:
        (str) first line of the poem
    """
    rand_1 = randint(0, len(word_dict['l1-adjective']) - 1)
    rand_2 = randint(0, len(word_dict['l1-noun']) - 1)
    a1 = word_dict['l1-adjective'][rand_1]
    n1 = word_dict['l1-noun'][rand_2]
    return a1 + ' ' + n1


def second_line() -> str:
    """
    makes the second line of the poem by taking random adjectives and nouns from p5_2words.py
    Returns:
        (str) second line of the poem
    """
    rand_1 = randint(0, len(word_dict['l2-adjective']) - 1)
    rand_2 = randint(0, len(word_dict['l2-adjective']) - 1)
    rand_3 = randint(0, len(word_dict['l2-adjective']) - 1)
    a1 = word_dict['l2-adjective'][rand_1]
    a2 = word_dict['l2-adjective'][rand_2]
    n1 = word_dict['l2-noun'][rand_3]
    return a1 + ' ' + a2 + ' ' + n1


def third_line() -> str:
    """
    makes the third and final line of the poem by taking random adjectives and nouns from p5_2words.py
    Returns:
        (str) third and final line of the poem
    """
    rand_1 = randint(0, len(word_dict['l3-adjective']) - 1)
    rand_2 = randint(0, len(word_dict['l3-noun']) - 1)
    a1 = word_dict['l3-adjective'][rand_1]
    n1 = word_dict['l3-noun'][rand_2]
    return a1 + ' ' + n1


def main():
    """
    driver function for our haiku generator
    Returns:
        none (function is null)
    """
    line_1 = first_line()
    line_2 = second_line()
    line_3 = third_line()
    print(line_1 + "\n", line_2 + "\n", line_3)


if __name__ == "__main__":
    main()
