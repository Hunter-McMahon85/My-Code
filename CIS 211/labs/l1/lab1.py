"""
Hunter McMahon
Lab1 - classes and objects
CIS 211
desc: lets get the term started eh
"""
import unittest


class Sentence:
    def __init__(self, sent_data: str,):
        self.__sent = sent_data

    def get_sentence(self):
        return self.__sent

    def get_words(self):
        sent_data = self.__sent
        return sent_data.split()

    def get_length(self):
        return len(self.__sent)

    def get_num_words(self):
        list_o_words = self.get_words()
        return len(list_o_words)
