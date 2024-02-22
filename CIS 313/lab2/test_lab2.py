import unittest
import pqueue
import mheap


class T0_pqueue_insert(unittest.TestCase):

    def test_1_pq_insert(self):
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        pq.insert(4)
        pq.insert(5)
        pq_list = [element for element in pq]
        self.assertEqual([5, 4, 2, 1, 3], pq_list)
        print("\n")


class T1_pqueue_peek(unittest.TestCase):

    def test_1_pq_peek(self):
        print("Just return the fist element of the queue.")
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        self.assertEqual(3, pq.peek())
        print("\n")


class T2_pqueue_extract_max(unittest.TestCase):

    def test_1_pq_extract_max(self):
        print("extract and return the maximum element of the queue")
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        self.assertEqual(3, pq.extract_max())
        print("\n")


class T3_build_heap(unittest.TestCase):

    def test_1_bh(self):
        # test build heap as if we enter an array into the heap when initiated, the build_heap() method must be called
        print("return the heap")
        print("\n")
        mh = mheap.max_heap(5, [1, 2, 3, 4, 5])
        self.assertEqual([5, 4, 3, 1, 2], mh.get_heap())
        print("\n")


class T5_heap_sort(unittest.TestCase):

    def test_heap_sort_1(self):
        print("\n")
        to_sort_list = [10, 24, 3, 57, 4, 67, 37, 87, 7]
        sorted_list = mheap.heap_sort(to_sort_list)
        self.assertEqual([3, 4, 7, 10, 24, 37, 57, 67, 87], sorted_list)
        print("\n")


class T6_insert_full_heap(unittest.TestCase):

    def test_full_heap_1(self):
        print("code should raise exception if we try to add value to full heap")
        print("\n")
        hm = mheap.max_heap(5)
        hm.insert(1)
        hm.insert(2)
        hm.insert(3)
        hm.insert(69)
        hm.insert(420)
        with self.assertRaises(Exception):
            hm.insert(720)
        print("\n")


class T7_extract_empty_heap(unittest.TestCase):

    def test_extract_empty_1(self):
        print("code should raise exception if we try to extract max an empty heap")
        print("\n")
        hm = mheap.max_heap(5)
        hm.insert(1)
        hm.insert(2)
        hm.insert(3)
        hm.insert(69)
        hm.extract_max()
        hm.extract_max()
        hm.extract_max()
        hm.extract_max()
        with self.assertRaises(Exception):
            hm.extract_max()
        print("\n")


class T8_pqueue_heap(unittest.TestCase):

    def test_1_pq_heap(self):
        print("\n")
        pq = pqueue.pqueue(30)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        pq.insert(4)
        pq.insert(5)
        pq.insert(69)
        pq.insert(420)
        pq.insert(14)
        pq.insert(360)
        pq.insert(50)
        pq.extract_max()
        pq.extract_max()
        pq.extract_max()
        pq.extract_max()
        pq.insert(51)
        pq.extract_max()
        pq.insert(51)
        pq.insert(60)
        pq.insert(53)
        pq.extract_max()
        pq.extract_max()
        pq.extract_max()
        pq.extract_max()
        pq_list = [element for element in pq]
        self.assertEqual([5, 4, 2, 1, 3], pq_list)
        print("\n")


# my own 6 test cases

class T4_heap_extract_max(unittest.TestCase):

    def test_1_heap_extract_max(self):
        print("extract and return the maximum element of the heap")
        print("\n")
        hm = mheap.max_heap(10)
        hm.insert(1)
        hm.insert(2)
        hm.insert(3)
        hm.insert(69)
        hm.insert(420)
        hm.insert(14)
        hm.insert(360)
        hm.insert(50)
        self.assertEqual(420, hm.extract_max())
        print("\n")


class T9_test_pq_isempty(unittest.TestCase):

    def test_pq_isempty(self):
        print("see if the pq is empty")
        print("\n")
        pq = pqueue.pqueue(5)
        self.assertEqual(True, pq.is_empty())
        print("\n")


class T10_heap_1(unittest.TestCase):
    def test_2_hp(self):
        print("\n")
        hp = pqueue.pqueue(5)
        hp.insert(4)
        hp.insert(3)
        hp.insert(6)
        hp.insert(10)
        hp.extract_max()
        hp_list = [element for element in hp]
        self.assertEqual([6, 3, 4], hp_list)
        print("\n")


class T11_heap_2(unittest.TestCase):
    def test_3_hp(self):
        print("\n")
        hp = pqueue.pqueue(5)
        hp.insert(100)
        hp.insert(50)
        hp.insert(25)
        hp.extract_max()
        hp.extract_max()
        hp.insert(40)
        hp.insert(55)
        hp_list = [element for element in hp]
        self.assertEqual([55, 25, 40], hp_list)
        print("\n")

"""
class T12_heap_3(unittest.TestCase):
    def test_4_hp(self):
        print("\n")
        hp = pqueue.pqueue(5)
        hp.insert(1)
        hp.insert(2)
        hp.insert(3)
        hp.insert(4)
        hp.insert(5)
        hp.extract_max()
        hp.extract_max()
        hp.extract_max()
        hp.extract_max()
        hp.extract_max()
        hp.insert(10)
        hp.extract_max()
        hp.insert(20)
        hp.insert(30)
        hp.extract_max()
        hp.insert(40)
        hp.insert(50)
        hp_list = [element for element in hp]
        self.assertEqual([50, 20, 40], hp_list)
        print("\n")
"""

class T13_heap_4(unittest.TestCase):
    def test_5_hp(self):
        print("\n")
        hp = pqueue.pqueue(10)
        hp.insert(69)
        hp.insert(35)
        hp.insert(21)
        hp.insert(46)
        hp.insert(500)
        hp.extract_max()
        hp.extract_max()
        hp.extract_max()
        hp.extract_max()
        hp_list = [element for element in hp]
        self.assertEqual([21], hp_list)
        print("\n")


if __name__ == '__main__':
    unittest.main()
