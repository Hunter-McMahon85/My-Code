import lab3
import unittest


# given
class T0_tree__insert(unittest.TestCase):

    def test_balanced_binary_search_tree(self):
        print("\n")
        print("tree_insert_with_individual_check")
        t = lab3.Tree()

        t.insert(4)
        t.insert(2)
        t.insert(6)
        t.insert(1)
        t.insert(3)
        t.insert(5)
        t.insert(7)

        # The following check is without using tree as an iterator (which uses inorder traversal)
        # So this function also does not check the implementation of the traversal function

        self.assertEqual(t.root.data, 4)
        self.assertEqual(t.root.left.data, 2)
        self.assertEqual(t.root.left.left.data, 1)
        self.assertEqual(t.root.left.right.data, 3)
        self.assertEqual(t.root.right.data, 6)
        self.assertEqual(t.root.right.left.data, 5)
        self.assertEqual(t.root.right.right.data, 7)

        print("\n")


class T1_min_and_max(unittest.TestCase):

    def test_min_and_max(self):
        print("\n")
        print("Checkin the min and the max functions")
        t = lab3.Tree()

        t.insert(4)
        t.insert(2)
        t.insert(6)
        t.insert(1)
        t.insert(3)
        t.insert(5)
        t.insert(7)

        minimum = t.min()
        self.assertEqual(1, minimum)
        maximum = t.max()
        self.assertEqual(7, maximum)

        print("\n")


class T2_Traversal(unittest.TestCase):

    def test_traversal(self):
        print("\n")
        print("Checking all the three traversals")
        t = lab3.Tree()

        t.insert(4)
        t.insert(2)
        t.insert(6)
        t.insert(1)
        t.insert(3)
        t.insert(5)
        t.insert(7)
        tree_iterator = [node for node in t]
        inorder = [node for node in t.inorder()]
        preorder = [node for node in t.preorder()]

        print("__iter__(): inorder traversal")
        self.assertEqual([1, 2, 3, 4, 5, 6, 7], tree_iterator)
        print("inorder traversal")
        self.assertEqual([1, 2, 3, 4, 5, 6, 7], inorder)
        print("preorder traversal")
        self.assertEqual([4, 2, 1, 3, 6, 5, 7], preorder)
        print("\n")


class T3_successor(unittest.TestCase):

    def test_successor(self):
        print("\n")
        print("successor function")
        tree_success = lab3.Tree()
        tree_success.insert(8)
        tree_success.insert(3)
        tree_success.insert(10)
        tree_success.insert(1)
        tree_success.insert(6)
        tree_success.insert(4)
        tree_success.insert(7)
        tree_success.insert(14)
        tree_success.insert(13)

        easy_success = tree_success.find_successor(8).data
        medium_success = tree_success.find_successor(10).data
        tough_success = tree_success.find_successor(7).data

        self.assertEqual(easy_success, 10)
        self.assertEqual(medium_success, 13)
        self.assertEqual(tough_success, 8)

        print("\n")


class T4_delete(unittest.TestCase):

    def test_delete(self):
        print("\n")
        print("delete function")
        t = lab3.Tree()
        t.insert(8)
        t.insert(3)
        t.insert(10)
        t.insert(1)
        t.insert(6)
        t.insert(4)
        t.insert(7)
        t.insert(14)
        t.insert(13)

        l1 = [node for node in t]
        t.delete(7)
        l2 = [node for node in t]
        t.delete(6)
        l3 = [node for node in t]
        t.delete(8)
        l4 = [node for node in t]
        t.delete(10)
        l5 = [node for node in t]

        self.assertEqual([1, 3, 4, 6, 7, 8, 10, 13, 14], l1)
        self.assertEqual([1, 3, 4, 6, 8, 10, 13, 14], l2)
        self.assertEqual([1, 3, 4, 8, 10, 13, 14], l3)
        self.assertEqual([1, 3, 4, 10, 13, 14], l4)
        self.assertEqual([1, 3, 4, 13, 14], l5)

        print("\n")


class T5_contains(unittest.TestCase):

    def test_contains(self):
        print("\n")
        print("contains function")
        t = lab3.Tree()
        t.insert(8)
        t.insert(3)
        t.insert(10)
        t.insert(1)
        t.insert(6)
        t.insert(4)
        t.insert(7)
        t.insert(14)
        t.insert(13)
        self.assertEqual(t.contains(13), True)
        self.assertEqual(t.contains(15), False)
        print("\n")


# custom

class T6_myinsert(unittest.TestCase):
    def test_my_insert(self):
        t = lab3.Tree()
        t.insert(18)
        t.insert(3)
        t.insert(16)
        t.insert(27)
        t.insert(1)
        t.insert(40)
        t.insert(42)
        t.insert(50)
        t.insert(23)
        t.insert(37)
        t.insert(31)
        t.insert(9)
        t.insert(38)
        t.insert(36)
        t.insert(12)
        t.insert(33)
        t.insert(24)
        t.insert(29)
        t.insert(44)
        t.insert(45)
        tree_inorder = [node for node in t.inorder()]
        self.assertEqual([1, 3, 9, 12, 16, 18, 23, 24, 27, 29, 31, 33, 36, 37, 38, 40, 42, 44, 45, 50], tree_inorder)


class T7_traverse(unittest.TestCase):
    def test_inorder_skewed(self):
        t = lab3.Tree()
        t.insert(10)
        t.insert(5)
        t.insert(8)
        t.insert(9)
        t.insert(7)
        t.insert(6)
        t.insert(4)
        t.insert(3)
        inorder = [node for node in t.inorder()]
        self.assertEqual([3, 4, 5, 6, 7, 8, 9, 10], inorder)

    def test_postorder(self):
        t = lab3.Tree()
        t.insert(10)
        t.insert(12)
        t.insert(8)
        t.insert(9)
        t.insert(17)
        t.insert(6)
        t.insert(14)
        t.insert(3)
        postorder = [node for node in t.postorder()]
        self.assertEqual([3, 6, 9, 8, 14, 17, 12, 10], postorder)

    def test_preorder_skewed(self):
        t = lab3.Tree()
        t.insert(10)
        t.insert(50)
        t.insert(35)
        t.insert(20)
        t.insert(17)
        t.insert(26)
        t.insert(38)
        t.insert(37)
        t.insert(15)
        t.insert(12)
        preorder = [node for node in t.preorder()]
        self.assertEqual([10, 50, 35, 20, 17, 15, 12, 26, 38, 37], preorder)


class T8_find_node(unittest.TestCase):
    def test_find_node(self):
        print("\n")
        print("contains method")
        t = lab3.Tree()
        t.insert(10)
        t.insert(2)
        t.insert(7)
        t.insert(1)
        t.insert(3)
        t.insert(5)
        t.insert(8)
        t.insert(6)

        self.assertEqual(t.root.left.right.left.right.right.data, t._Tree__find_node(6).data)
        self.assertEqual(None, t._Tree__find_node(20))
        print("\n")


class T9_contains(unittest.TestCase):
    def test_contains(self):
        print("\n")
        print("contains method")
        t = lab3.Tree()

        t.insert(4)
        t.insert(2)
        t.insert(6)
        t.insert(1)
        t.insert(3)
        t.insert(5)
        t.insert(7)
        self.assertEqual(True, t.contains(6))
        self.assertEqual(False, t.contains(69))
        print("\n")


class T10_successor(unittest.TestCase):
    def test_find_successor(self):
        print("\n")
        print("successor function")
        tree_success = lab3.Tree()
        tree_success.insert(8)
        tree_success.insert(3)
        tree_success.insert(10)
        tree_success.insert(1)
        tree_success.insert(6)
        tree_success.insert(4)
        tree_success.insert(7)
        tree_success.insert(24)
        tree_success.insert(22)
        tree_success.insert(25)
        tree_success.insert(21)
        tree_success.insert(20)
        tree_success.insert(19)
        tree_success.insert(18)
        tree_success.insert(17)

        left_success = tree_success.find_successor(10).data

        self.assertEqual(17, left_success)

        print("\n")

    def test_find_successor2(self):
        def test_find_successor(self):
            print("\n")
            print("successor function")
            tree_success = lab3.Tree()
            tree_success.insert(8)
            tree_success.insert(3)
            tree_success.insert(1)
            tree_success.insert(4)
            tree_success.insert(6)
            tree_success.insert(7)
            tree_success.insert(10)
            tree_success.insert(13)
            tree_success.insert(14)

            success = tree_success.find_successor(14).data

            self.assertEqual(None, success)

            print("\n")


    def test_find_successor_special(self):
        print("\n")
        print("successor function")
        tree_success = lab3.Tree()
        tree_success.insert(8)
        tree_success.insert(3)

        left_success = tree_success.find_successor(3).data
        root_succ = tree_success.find_successor(8)

        self.assertEqual(8, left_success)
        self.assertEqual(None, root_succ)

        print("\n")


class T11_delete(unittest.TestCase):
    def test_delete(self):
        t = lab3.Tree()
        t.insert(10)
        t.insert(5)
        t.insert(3)
        t.insert(4)
        t.insert(7)
        t.insert(6)
        t.insert(15)
        t.insert(21)
        t.delete(10)
        t.delete(5)
        t.delete(3)
        t.delete(7)
        t.delete(6)
        t1 = [node for node in t.inorder()]
        self.assertEqual([4, 15, 21], t1)


class T12_keyerrors(unittest.TestCase):
    def test_empty_find_successor(self):
        t = lab3.Tree()
        with self.assertRaises(KeyError):
            t.find_successor(20)

    def test_empty_delete(self):
        t = lab3.Tree()
        with self.assertRaises(KeyError):
            t.delete(20)


class T13_min_and_max(unittest.TestCase):
    def test_min_and_max(self):
        print("\n")
        print("Checkin the min and the max functions")
        t = lab3.Tree()

        minimum = t.min()
        self.assertEqual(None, minimum)
        maximum = t.max()
        self.assertEqual(None, maximum)

        t.insert(2)

        minimum = t.min()
        self.assertEqual(2, minimum)
        maximum = t.max()
        self.assertEqual(2, maximum)

        print("\n")

if __name__ == '__main__':
    unittest.main()
