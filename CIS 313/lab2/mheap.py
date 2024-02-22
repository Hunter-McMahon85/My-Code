class max_heap(object):
    """
    Binary max-heap

    Supports most standard heap operations (insert, peek, extract_max).
    Can be used for building a priority queue or heapsort. Since Python
    doesn't have built-in arrays, the underlying implementation uses a
    Python list instead. When initialized, max_heap creates a new list of
    fixed size or uses an existing list.

    initialization args:
        size [int] : max size allocated for the heap
        data [list] : a predefined data list to be turned into a heap object

    methods:

    __init__ :
        initializes the heap, sets the following attributes:
            max_size : the maximum size allocated for the heap
            heap : the list with heap values
            length : the current amount of entries in the heap

    get_heap:
        returns the heap as a list

    insert(data):
        adds a new data entry into the heap and calls build_heap()
        to ensure that heap is in compliance with the heap rule
        raises index error if heap is full

    peek:
        returns the max value of the heap

    extract_max:
        removes and returns the max value of the heap and adjust the heap in reaction to the value being removed

    __heapify(curr_index, list_length=none):
        takes an index on the tree and recursively checks to see if it and its children abide by the heap rules

    build_heap:
        loops through __heapify to ensure that self.heap is actually a heap

    def __get_parent(loc):
        gets index of loc's parent

    def __get_left(loc):
        gets index of loc's left child

    def __get_right(self, loc):
        gets index of loc's right child

    def __swap(a, b):
        swaps items of index a and b in heap

    """

    def __init__(self, size=20, data=None):
        """Initialize a binary max-heap.

        size: Total capacity of the heap.
        data: List containing the desired heap contents. 
              The list is used in-place, not copied, so its contents 
              will be modified by heap operations.
              If data is specified, then the size field is ignored."""

        # Add to this constructor as needed
        if data is not None:
            self.max_size = len(data)
            self.heap = data
            self.length = len(data) - 1
            self.build_heap()
        else:
            self.max_size = size
            self.length = 0
            self.heap = [None] * size

    def get_heap(self):
        return self.heap

    def insert(self, data):
        """
        Insert an element into the heap.

        Raises IndexError if the heap is full.
        """
        try:
            if self.length == self.max_size:
                raise IndexError
            else:
                if self.length == 0:
                    self.heap[self.length] = data
                else:
                    self.heap[self.length] = data
                    self.build_heap()
                self.length += 1
        except IndexError:
            print("IndexError: Heap is Full")
            raise IndexError

    def peek(self):
        """Return the maximum value in the heap."""
        return self.heap[0]

    def extract_max(self):
        """Remove and return the maximum value in the heap.

        Raises KeyError if the heap is empty."""
        # Tips: Maximum element is first element of the list
        #     : swap first element with the last element of the list.
        #     : Remove that last element from the list and return it.
        #     : call __heapify to fix the heap
        try:
            if self.heap[0] is None:
                raise KeyError
            else:
                self.length -= 1
                head_max = self.heap[0]
                self.__swap(0, self.length)
                del self.heap[self.length]
                if self.length != -1:
                    self.build_heap()
                self.heap.append(None)
                return head_max
        except KeyError:
            print("KeyError: Heap is empty, cant extract max")
            raise KeyError

    def __heapify(self, curr_index, list_length=None):
        """
        verifies that a value at an index in the heap complies with the heap rule.
        args:
            curr_index (int): the index we are checking to see if it complies with the heap
            list_length (int): the length of the list (None if not specified)
        return:
            none
        """
        largest = curr_index
        left = self.__get_left(curr_index)
        right = self.__get_right(curr_index)
        if left <= self.length:
            if self.heap[left] is not None:
                if self.heap[curr_index] < self.heap[left]:
                    largest = left
        if right <= self.length:
            if self.heap[right] is not None:
                if self.heap[largest] < self.heap[right]:
                    largest = right
        if largest != curr_index:
            self.__swap(curr_index, largest)
            self.__heapify(largest)

    def build_heap(self):
        """
        Loops Heapify to ensure that the tree is a proper heap
        Return:
            Void
        """
        # lower limit of n/2, need this for the parents
        j = (self.length - 1 // 2)
        # loops from the lowest parents in the tree upwards and runs heapify at each point
        # to ensure that the tree is still a proper heap
        for i in range(j, -1, -1):
            self.__heapify(i)

    ''' Optional helper methods may be used if required '''
    ''' You may create your own helper methods as required.'''
    ''' But do not modify the function definitions of any of the above methods'''

    def __get_parent(self, loc):
        # left child has odd location index
        # right child has even location index
        # if loc % 2 == 0:
        #     parent = int((loc - 2) / 2)
        # else:
        parent = int((loc - 1) / 2)
        return parent

    def __get_left(self, loc):
        return 2 * loc + 1

    def __get_right(self, loc):
        return 2 * loc + 2

    def __swap(self, a, b):
        # swap elements located at indexes a and b of the heap
        temp = self.heap[a]
        self.heap[a] = self.heap[b]
        self.heap[b] = temp


def heap_sort(l):
    """Sort a list in place using heapsort."""
    # Note: the heap sort function is outside the class
    #     : The sorted list should be in ascending order
    # Tips: Initialize a heap using the provided list
    #     : Use build_heap() to turn the list into a valid heap
    #     : Repeatedly extract the maximum and place it at the end of the list
    #     : Refer page 161 in the CLRS textbook for the exact procedure
    ascending_list = []
    heap_list = max_heap(len(l), l)
    for i in range(heap_list.length + 1):
        ascending_list.insert(0, heap_list.extract_max())
    return ascending_list
