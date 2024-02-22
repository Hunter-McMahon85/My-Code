"""
Hunter McMahon
CIS 211
lab 1 unit test
first time using unit test
"""
import unittest
from lab1 import Sentence


class T0_SentenceLength(unittest.TestCase):
    """Test the methods of the sentence class. Note that you can
       also create multiple test classes -- one per method."""

    def test_get_length_nonempty(self):
        """Check whether the length of a sentence is correct"""
        the_sentence_obj = Sentence('Hello world')
        self.assertEqual(the_sentence_obj.get_length(), 11)

    def test_get_length_empty(self):
        """Check whether the length of a sentence is correct"""
        the_sentence_obj = Sentence('')
        self.assertEqual(the_sentence_obj.get_length(), 0)

    # ... TODO: add your test classes here, e.g., T1_WordList, T2_Getter, ...
    def test_getting_words_empty(self):
        """checks to see if the returned list of words is correct"""
        sent_obj = Sentence("")
        self.assertEqual(sent_obj.get_words(), [])

    def test_getting_words(self):
        """checks to see if the returned list of words is correct"""
        sent_obj = Sentence("hello world")
        self.assertEqual(sent_obj.get_words(), ["hello", "world"])

    def test_getting_sentence(self):
        """checks to see if the returned sentence is correct"""
        sent_obj = Sentence("hello world")
        self.assertEqual(sent_obj.get_sentence(), "hello world")

    def test_getting_word_count(self):
        """checks to see if the returned # of words"""
        sent_obj = Sentence("hello world")
        self.assertEqual(sent_obj.get_num_words(), 2)

    # template:
    # in the future make a individual seprate class for each method that needs to be tested
    """
    import unittest
    import file
        or 
    from file import class
    
    class name(unittest.testcase):
        def testname(self):
            object_variable = example of object
            self.assertEqual(object_variable.object_method(), expected output)
            
    
    
    """


if __name__ == "__main__":
    unittest.main(verbosity=2)

if __name__ == '__main__':
    unittest.main()
