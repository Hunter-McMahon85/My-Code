"""
Hunter McMahon
Cis 122
description: have some sentence stats
"""
import doctest


def sentence_stats(a_sentence: str):
    """
    takes a sentence string and finds the averages word length
    Args:
        a_sentence: (str) a sentence we want some stats off

    Returns:
        average word length
    >>> sentence_stats("Never gonna give you up")
    3.8
    >>> sentence_stats("Never gonna let you down")
    4.0
    >>> sentence_stats("Never gonna run around and desert you")
    4.428571428571429
    >>> sentence_stats("Never gonna make you cry")
    4.0
    >>> sentence_stats("Never gonna say goodbye")
    5.0
    >>> sentence_stats("Never gonna tell a lie and hurt you")
    3.5


    """
    words = a_sentence.split(' ')
    total_length = 0
    number_of_words = 0
    for i in range(len(words)):
        total_length += len(words[i])
        number_of_words += 1
    average_length = total_length / number_of_words
    return average_length


def main():
    """
    handles input, runs it through sentence_stats, and prints result
    Returns:
        none
    """
    sentence = input("Please enter a sentence:")
    awl = sentence_stats(sentence)
    print("The average word length is: ", awl)


print(doctest.testmod())
