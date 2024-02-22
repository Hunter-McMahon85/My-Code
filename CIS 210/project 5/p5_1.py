"""
Hunter McMahon
CIS 210
P5 pt 1
description: The words numbers, the numbers, what do they mean?
"""


# Implement your solutions here. Remember to follow 210 Style and PEP8.
# Do not forget to click SUBMIT -- you can submit multiple times without penalty.
#
# Include doctests whenever appropriate. Feel free to delete these comments.
# To run doctests, at the "Console" below, type: python -m doctest p5_1.py -v

def get_user_input() -> list:
    """
    prompts the user for some input
    Returns:
        the sentence input as a list of lines for the main function
    """
    print('Enter some Sentences to calculate Stats (Ctrl-D, Cmd-D or Ctrl-Z (Windows) to end):')
    entered_lines = []
    while True:
        try:
            entry_line = input()
        except EOFError:
            break
        entered_lines.append(entry_line)
    return entered_lines


def get_num_words(text_lines: list) -> int:
    """
    takes an list of entered lines and finds out how many words are in it
    Args:
        text_lines:
            (list) the lines we want the wordcount of
    Returns:
        (int) the number of words in the entry
        >>> get_num_words([])
        0
        >>> get_num_words(['one two\\n', 'three\\n', 'four'])
        4
    """
    num_o_words = 0
    for i in range(len(text_lines)):
        words = text_lines[i].split()
        num_o_words += len(words)
    return num_o_words


def get_num_sentences(text_lines: list) -> int:
    """
    takes the text lines and finds how many sentences are in them based on punctuation
    Args:
        text_lines:
            (list) the list of text we are finding the sentence count of
    Returns:
        (int) the amount of sentences in the lines

        >>> get_num_sentences([])
        0
        >>> get_num_sentences(['This is the first!', 'I am second. Am I third?'])
        3
    """
    num_o_sentences = 0
    lines_words = []
    for i in range(len(text_lines)):
        lines_words += text_lines[i].split()
    for i in range(len(lines_words)):
        ending_character = lines_words[i][-1]
        if ending_character in ".?!":
            num_o_sentences += 1
    return num_o_sentences


def get_avg_words(num_words: int, num_sentences: int) -> float:
    """
    calculates the average number of words per sentence given the number of both (rounded to 1 digit)
    Args:
        num_words:
            (int) the word count of the text lines
        num_sentences:
            (int) the number of sentences in the text lines
    Returns:
        (float) the average number of words per sentence rounded to one decimal

    >>> get_avg_words(10, 3)
    3.3
    >>> get_avg_words(10, 0)
    Traceback (most recent call last):
    ...
    ZeroDivisionError: float division by zero

    """
    # the + 0.0 is not necessary but rather ensures the float division by zero error in that case
    average_word_sent_count = (num_words + 0.0) / (num_sentences + 0.0)
    return round(average_word_sent_count, 1)


def get_most_used_word(text_lines: list) -> str:
    """
    figures out the most used word in the entered lines
    Args:
        text_lines:
            (list) the lines which we will examine to find the most used word
    Returns:
        (str) the most used word
    >>> get_most_used_word(["duck duck goose!","DUCK, DUCK, GOOSE!"])
    'duck'
    >>> get_most_used_word(["Hello... Is it me you're looking for?"])
    'hello'
    """
    lines_words = []
    most_used = ""
    most_times_used = 0
    for i in range(len(text_lines)):
        lines_words += text_lines[i].split()
    for i in range(len(lines_words)):
        og_word = lines_words[i]
        word = ""
        # remove punctuation
        # todo: fix punctuation filter
        for c in og_word:
            if c not in ",.:;?!()*@%$<>/][{}":
                word += c
        word_occurrence = lines_words.count(og_word)
        if word_occurrence > most_times_used:
            most_used = word.lower()
            most_times_used = word_occurrence
    return most_used


def print_stats(num_words: int, num_sentences: int, sent_avg_words: float, most_freq_word: str):
    """
    prints out the stats that were found in each function in a formatted table
    Args:
        num_words:
            (str) the number of words in the entry
        num_sentences:
            (str) the number of sentences in the entry
        sent_avg_words:
            (str) the average number of words per sentence in the entry
        most_freq_word:
            (str) the most used word in the entry
    Returns:
        none, function is void
    >>> print_stats(55, 4, 13.8, 'and')
           Sentence Statistics Table
    ----------------------------------------
    | Number of words        |          55 |
    | Number of sentences    |           4 |
    | Average words/sentence |        13.8 |
    | Most frequent word     |         and |
    ----------------------------------------
    >>> print_stats(0, 0, 0, '')
           Sentence Statistics Table
    ----------------------------------------
    | Number of words        |           0 |
    | Number of sentences    |           0 |
    | Average words/sentence |         0.0 |
    | Most frequent word     |             |
    ----------------------------------------
    """
    word_num = str(num_words)
    sentences_num = str(num_sentences)
    word_avg = str(float(sent_avg_words))
    print('Sentence Statistics Table'.rjust(32))
    print('-' * 40)
    print('|', 'Number of words', '|'.rjust(8), word_num.rjust(11), '|')
    print('|', 'Number of sentences', '|'.rjust(4), sentences_num.rjust(11), '|')
    print('|', 'Average words/sentence', '|', word_avg.rjust(11), '|')
    print('|', 'Most frequent word', '|'.rjust(5), most_freq_word.rjust(11), '|')
    print("-" * 40)


# --- You should not have to modify main() -----
def main():
    """Driver function: calls other functions to perform all tasks."""
    lines = get_user_input()
    num_words = get_num_words(lines)
    num_sentences = get_num_sentences(lines)
    avg_words = get_avg_words(num_words, num_sentences)
    most_freq_word = get_most_used_word(lines)
    print_stats(num_words, num_sentences, avg_words, most_freq_word)


if __name__ == '__main__':
    main()
