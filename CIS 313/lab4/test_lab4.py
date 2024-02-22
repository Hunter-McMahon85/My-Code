from rb_tree import Node, rb_tree
import unittest


class T0_tree_left_rotation(unittest.TestCase):

    def test_tree_left_rotation_1(self):
        print("\n")
        print("tree_left_rotation")
        tree = rb_tree()
        tree.bst_insert(2)
        tree.bst_insert(1)
        tree.bst_insert(3)
        tree.print_tree()
        print("initial preorder tree", "\n")
        tree.left_rotate(tree.root)
        tree_preorder = [node.data for node in tree.preorder()]
        self.assertEqual([3, 2, 1], tree_preorder)
        tree.print_tree()
        print("tree after left rotation about root  in preorder")
        print("\n")

    def test_tree_left_rotation_2(self):
        print("\n")
        print("tree_left_rotation")
        tree = rb_tree()
        tree.bst_insert(7)
        tree.bst_insert(5)
        tree.bst_insert(9)
        tree.bst_insert(3)
        tree.bst_insert(6)
        tree.bst_insert(8)
        tree.bst_insert(10)
        tree.bst_insert(1)
        tree.bst_insert(2)
        tree.print_tree()
        print("initial preorder tree", "\n")
        tree.left_rotate(tree.root)
        tree_preorder = [node.data for node in tree.preorder()]
        self.assertEqual([9, 7, 5, 3, 1, 2, 6, 8, 10], tree_preorder)
        tree.print_tree()
        print("tree after left rotation about root  in preorder")
        print("\n")

    # my defined test

    def test_tree_left_rotation_3(self):
        print("\n")
        print("tree_left_rotation key error")
        tree = rb_tree()
        tree.bst_insert(7)
        tree.bst_insert(5)
        tree.bst_insert(4)
        tree.bst_insert(3)
        tree.print_tree()
        print("initial preorder tree", "\n")
        with self.assertRaises(KeyError):
            tree.left_rotate(tree.root)
        tree.print_tree()
        print("tree after left rotation about root  in preorder")
        print("\n")

    def test_tree_left_rotation_4(self):
        print("\n")
        print("tree_left_rotation key error")
        tree = rb_tree()
        tree.bst_insert(7)
        tree.print_tree()
        print("initial preorder tree", "\n")
        with self.assertRaises(KeyError):
            tree.left_rotate(tree.root)
        tree.print_tree()
        print("tree after left rotation about root  in preorder")
        print("\n")

    def test_tree_left_rotation_5(self):
        print("\n")
        print("tree_left_rotation key error empty tree")
        tree = rb_tree()
        with self.assertRaises(KeyError):
            tree.left_rotate(tree.root)
        print("\n")


class T1_tree_right_rotation(unittest.TestCase):

    def test_tree_right_rotation_1(self):
        print("\n")
        print("tree_right_rotation")
        tree = rb_tree()
        tree.bst_insert(2)
        tree.bst_insert(1)
        tree.bst_insert(3)

        tree.print_tree()
        print("initial preorder tree", "\n")
        tree.right_rotate(tree.root)
        tree_preorder = [node.data for node in tree.preorder()]
        self.assertEqual([1, 2, 3], tree_preorder)
        tree.print_tree()
        print("tree after right rotation about root  in preorder")
        print("\n")

    def test_tree_right_rotation_2(self):
        print("\n")
        print("tree_right_rotation")
        tree = rb_tree()
        tree.bst_insert(7)
        tree.bst_insert(5)
        tree.bst_insert(9)
        tree.bst_insert(3)
        tree.bst_insert(6)
        tree.bst_insert(8)
        tree.bst_insert(10)
        tree.bst_insert(1)
        tree.bst_insert(2)
        tree.print_tree()
        print("initial preorder tree", "\n")
        tree.right_rotate(tree.root)
        tree_preorder = [node.data for node in tree.preorder()]
        self.assertEqual([5, 3, 1, 2, 7, 6, 9, 8, 10], tree_preorder)
        tree.print_tree()
        print("tree after right rotation about root  in preorder")
        print("\n")

    # my defined test cases
    def test_tree_right_rotation_3(self):
        print("\n")
        print("tree_right_rotation key error")
        tree = rb_tree()
        tree.bst_insert(7)
        tree.bst_insert(10)
        tree.bst_insert(20)
        tree.bst_insert(15)
        tree.print_tree()
        print("initial preorder tree", "\n")
        with self.assertRaises(KeyError):
            tree.right_rotate(tree.root)
        tree.print_tree()
        print("tree after right rotation about root  in preorder")
        print("\n")

    def test_tree_right_rotation_4(self):
        print("\n")
        print("tree_right_rotation key error 1 node")
        tree = rb_tree()
        tree.bst_insert(7)
        tree.print_tree()
        print("initial preorder tree", "\n")
        with self.assertRaises(KeyError):
            tree.right_rotate(tree.root)
        tree.print_tree()
        print("tree after right rotation about root  in preorder")
        print("\n")

    def test_tree_right_rotation_5(self):
        print("\n")
        print("tree_right_rotation key error empty tree")
        tree = rb_tree()
        with self.assertRaises(KeyError):
            tree.left_rotate(tree.root)
        print("\n")


class T2_tree_insert_color(unittest.TestCase):

    def test_tree_insert_color_0(self):
        print("\n")
        print("tree_color_check")

        tree = rb_tree()

        tree.insert(2)
        tree.insert(1)
        tree.insert(3)
        tree.insert(4)
        tree.print_tree()
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual([2, 1, 3, 4], tree_preorder)
        self.assertEqual(['black', 'black', 'black', 'red'], tree_preorder_color)
        print("\n")

    def test_tree_insert_color_1(self):
        print("\n")
        print("tree_color_check")

        tree = rb_tree()

        for i in range(1, 8):
            tree.insert(i)
        tree.print_tree()
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual([2, 1, 4, 3, 6, 5, 7], tree_preorder)
        self.assertEqual(['black', 'black', 'red', 'black', 'black', 'red', 'red'], tree_preorder_color)
        print("\n")

    def test_tree_insert_color_2(self):
        print("\n")
        print("tree_color_check 2")

        tree = rb_tree()
        tree.insert(7)
        tree.insert(5)
        tree.insert(9)
        tree.insert(3)
        tree.insert(6)
        tree.insert(8)
        tree.insert(10)
        tree.insert(1)
        tree.insert(2)
        tree.print_tree()
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual([7, 5, 2, 1, 3, 6, 9, 8, 10], tree_preorder)
        self.assertEqual(['black', 'red', 'black', 'red', 'red', 'black', 'black', 'red', 'red'], tree_preorder_color)
        print("\n")

    # my test cases

    def test_tree_insert_color_3(self):
        print("\n")
        print("tree_color_check 2 element")

        tree = rb_tree()

        tree.insert(14)
        tree.insert(6)
        tree.print_tree()
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual([14, 6], tree_preorder)
        self.assertEqual(['black',  'red'], tree_preorder_color)
        print("\n")

    def test_tree_insert_color_4(self):
        print("\n")
        print("tree_color_check unbalanced left before rotation")

        tree = rb_tree()

        tree.insert(14)
        tree.insert(6)
        tree.insert(9)
        tree.print_tree()
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual([9, 6, 14], tree_preorder)
        self.assertEqual(['black', 'red', 'red'], tree_preorder_color)
        print("\n")

    def test_tree_insert_color_5(self):
        print("\n")
        print("tree_color_check unbalanced right before rotation")

        tree = rb_tree()
        tree.insert(6)
        tree.insert(14)
        tree.insert(20)
        tree.insert(9)
        tree.print_tree()
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual([14, 6, 9, 20], tree_preorder)
        self.assertEqual(['black', 'black', 'red', 'black'], tree_preorder_color)
        print("\n")


class T3_tree_delete(unittest.TestCase):

    def test_tree_delete_0(self):
        print("\n")
        print("tree_insert")
        # print("checking in order, preorder and post order")
        tree = rb_tree()

        tree.insert(7)
        tree.insert(5)
        tree.insert(9)
        tree.insert(6)
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual([7, 5, 6, 9], tree_preorder)
        self.assertEqual(['black', 'black', 'red', 'black'], tree_preorder_color)
        tree.delete(9)
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual([6, 5, 7], tree_preorder)
        self.assertEqual(['black', 'black', 'black'], tree_preorder_color)
        print("\n")

    def test_tree_delete_1(self):
        print("\n")
        print("tree_insert")
        print("checking in order, preorder and post order")
        tree = rb_tree()

        for i in range(1, 8):
            tree.insert(i)
        tree.delete(5)
        tree.delete(4)
        # tree.print_tree()
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual([2, 1, 6, 3, 7], tree_preorder)
        self.assertEqual(['black', 'black', 'red', 'black', 'black'], tree_preorder_color)
        print("\n")

    def test_tree_delete_color_2(self):
        print("\n")
        print("tree_left_rotation")
        tree = rb_tree()
        tree.insert(7)
        tree.insert(5)
        tree.insert(9)
        tree.insert(3)
        tree.insert(6)
        tree.insert(8)
        tree.insert(10)
        tree.insert(1)
        tree.insert(2)
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual([7, 5, 2, 1, 3, 6, 9, 8, 10], tree_preorder)
        self.assertEqual(['black', 'red', 'black', 'red', 'red', 'black', 'black', 'red', 'red'], tree_preorder_color)
        tree.delete(6)
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual([7, 2, 1, 5, 3, 9, 8, 10], tree_preorder)
        self.assertEqual(['black', 'red', 'black', 'black', 'red', 'black', 'red', 'red'], tree_preorder_color)
        tree.delete(7)
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual([8, 2, 1, 5, 3, 9, 10], tree_preorder)
        self.assertEqual(['black', 'red', 'black', 'black', 'red', 'black', 'red'], tree_preorder_color)
        print("\n")

    # my test cases

    def test_tree_delete_3(self):
        print("\n")
        print("check tree delete with only 1 element in tree")

        tree = rb_tree()

        tree.insert(14)
        tree.print_tree()
        tree.delete(14)
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual([], tree_preorder)
        self.assertEqual([], tree_preorder_color)
        print("\n")

    def test_tree_delete_4(self):
        print("\n")
        print("check tree delete with only 3 element in tree and node deletion")

        tree = rb_tree()

        tree.insert(5)
        tree.insert(4)
        tree.insert(6)
        tree.print_tree()
        tree.delete(5)
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual([6,4], tree_preorder)
        self.assertEqual(['black', 'red'], tree_preorder_color)
        print("\n")

    def test_tree_delete_5(self):
        print("\n")
        print("check a series of insertions and deletions")
        tree = rb_tree()

        tree.insert(5)
        tree.insert(4)
        tree.insert(6)
        tree.insert(9)
        tree.delete(5)
        tree.insert(42)
        tree.insert(12)
        tree.delete(42)
        tree.insert(29)
        tree.insert(26)
        tree.insert(7)
        tree.delete(12)
        tree.delete(26)
        tree.print_tree()
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual([6, 4, 9, 7, 29], tree_preorder)
        self.assertEqual(['black', 'black', 'red', 'black', 'black'], tree_preorder_color)
        print("\n")

if __name__ == "__main__":
    unittest.main()
