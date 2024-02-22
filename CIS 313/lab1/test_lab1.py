import lab1
import unittest


# note that in the given code the placement of the expected and actual values in the unit test was the wrong way around

class T0_TestingQueue(unittest.TestCase):

    def test_str(self):
        # testing the basic __str__() operation
        print("\n")
        q = lab1.Queue()
        self.assertEqual('[]', q.__str__())
        q.enqueue(1)
        self.assertEqual('[1]', q.__str__())
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        self.assertEqual('[1, 2, 3, 4]', q.__str__())
        print("\n")

    def test_basic_enqueue(self):
        # testing the basic enqueue operation
        print("\n")
        q = lab1.Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)

        self.assertEqual('[1, 2, 3, 4]', q.__str__())
        print("\n")

    def test_basic_dequeue(self):
        # testing the basic dequeue operation
        print("\n")
        q = lab1.Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        q.dequeue()
        q.dequeue()
        self.assertEqual('[3, 4]', q.__str__())
        q.dequeue()
        q.dequeue()
        self.assertEqual('[]', q.__str__())
        with self.assertRaises(Exception):
            q.dequeue()
        print("\n")

    def test_isempty(self):
        # testing the basic dequeue operation
        print("\n")
        q = lab1.Queue()
        self.assertEqual(True, q.isEmpty())
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        self.assertEqual(False, q.isEmpty())
        print("\n")


class T1_TestingStack(unittest.TestCase):

    def test_str(self):
        print("\n")
        s = lab1.Stack()
        self.assertEqual("[]", s.__str__())
        s.push("4")
        self.assertEqual("[4]", s.__str__())
        s.push("3")
        s.push("2")
        s.push("1")
        self.assertEqual("[1, 2, 3, 4]", s.__str__())
        print("\n")

    def test_push(self):
        # testing if queue is empty
        print("\n")
        s = lab1.Stack()
        s.push("4")
        s.push("3")
        s.push("2")
        s.push("1")
        self.assertEqual("[1, 2, 3, 4]", s.__str__())
        print("\n")

    def test_pop(self):
        # testing if queue is empty
        print("\n")
        s = lab1.Stack()
        s.push("4")
        s.push("3")
        s.push("2")
        s.push("1")
        s.pop()
        s.pop()
        self.assertEqual("[3, 4]", s.__str__())
        print("\n")

    def test_is_empty_false(self):
        # testing if queue is empty
        print("\n")
        s = lab1.Stack()
        s.push("4")
        print("return false if the stack is not empty")
        self.assertEqual(False, s.isEmpty())
        print("\n")

    def test_is_empty_true(self):
        # testing if queue is empty
        print("\n")
        s = lab1.Stack()
        print("return True if the stack is empty")
        self.assertEqual(True, s.isEmpty())
        print("\n")


class T2_TestingPalindrome(unittest.TestCase):

    def test_basic_string(self):
        # testing with basic string
        print("\n")
        string = "hello"
        p = lab1.isPalindrome(string)
        print("The string being tested is -> ", string)
        self.assertEqual(False, p)
        print("\n")

    def test_long_string(self):
        # testing with basic string
        print("\n")
        string = "rgf9qgfwqgdf097g3f7!@#$%&*(*)agsf8qlauofcgbeudgbcb;fbvaoubcj"
        p = lab1.isPalindrome(string)
        print("The string being tested is -> ", string)
        self.assertEqual(False, p)
        print("\n")

    def test_palindrome_simple(self):
        # testing with basic string
        print("\n")
        string = "TaCo CaT"
        p = lab1.isPalindrome(string)
        print("The string being tested is -> ", string)
        self.assertEqual(True, p)
        print("\n")

    def test_palindrome_longer(self):
        # testing with basic string
        print("\n")
        string = "96 6aa@@aa6 69"
        p = lab1.isPalindrome(string)
        print("The string being tested is -> ", string)
        self.assertEqual(True, p)
        print("\n")


if __name__ == '__main__':
    unittest.main()
