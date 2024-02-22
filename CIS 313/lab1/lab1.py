"""
Hunter McMahon
CS313
Lab 1
Some things with queues and dequeues
"""

class Node(object):
    """
    A class to represent a node.

    ...

    Attributes
    ----------
    data : int or float
        An individual character or number to be stored in a node
    next_node : object of class Node
        A pointer to the next node in a stack or queue

    Methods
    -------
    setData(data):
        Updates the value of data attribute of Node
    setNext(next_node):
        Updates the value of next_node attribute of Node
    getData():
        Returns the value of data attribute
    getNext():
        Returns the value of next_node attribute
    """

    def __init__(self, data=None, next_node=None):
        """
        Constructs (or initializes) the attributes for an object of the class

        ...

        Parameters
        ----------
        data : int or float
            An individual character or number to be stored in a node
        next_node : object of class Node
            A pointer to the next node in a stack or queue

        """
        self.__data = data
        self.__next_node = next_node

    def setData(self, data):
        """Set the "data" data field to the corresponding input."""
        self.__data = data

    def setNext(self, next_node):
        """Set the "next_node" data field to the corresponding input."""
        self.__next_node = next_node

    def getData(self):
        """Return the "data" data field."""
        return self.__data

    def getNext(self):
        """Return the "next_node" data field."""
        return self.__next_node


class Queue(object):
    """
    class that uses nodes to form a queue, a data structure where the First object in is the first object out.
    ...

    Attributes
    ----------
    there are no attributes

    Methods
    -------
    __str__(self):
        Returns the data in queue as a string
    enqueue(self, newData):
        Adds an item to the end of the queue
    dequeue(self):
        Returns and removes the first item that was put into the queue
    isEmpty(self):
        Checks to see if the queue is empty and then returns a boolean
    """

    def __init__(self):
        self.__head = None
        self.__tail = None

    def __str__(self):
        """
        Returns the data of the queue as a nice string
        Returns
        -------
            data_string (str): queue data as a string
        """
        # initiate some function vars
        data_string = ""
        i = True
        next_2_add = self.__head

        # checks to see if we have any values in queue or if there is only one item in queue before going to a loop
        if isinstance(next_2_add, Node):
            # if we have an head item, add it to the STR
            data_string = "[" + str(next_2_add.getData())
            # check to see if its alone, if so then we prevent the loop
            if isinstance(next_2_add.getNext(), Node):
                next_2_add = next_2_add.getNext()
            # prevents loop if the queue has 1 item
            else:
                i = False
        else:
            # prevents loop if the queue has no items
            data_string += "["
            i = False

        while i:
            # checks to see if the next value is another Node or None (the end of the Queue) then updates next_to_add
            # to be the the next Node if it exist
            if isinstance(next_2_add, Node):
                data_string += ", " + str(next_2_add.getData())
                next_2_add = next_2_add.getNext()
            # stops the loop if the next_2_add var is none indicating end of queue
            else:
                i = False
        data_string += "]"
        return data_string

    def enqueue(self, newData):
        """
        adds a new item to the queue
        Parameters
        ----------
        newData: data to be added to the queue

        Returns
        -------
            None, function is void
        """
        # Hint: Think about what's different for the first node added to the Queue
        if self.__head is None:
            self.__head = Node(newData)
            self.__tail = self.__head
        else:
            self.__tail.setNext(Node(newData))
            self.__tail = self.__tail.getNext()

    def dequeue(self):
        """
        removes the oldest item in the queue
        Returns
        -------
        prev_head: the old head of the queue which is the oldest item of the queue
        """
        try:
            if self.__head == None:
                raise Exception
            else:
                prev_head = self.__head.getData()
                self.__head = self.__head.getNext()
                return prev_head
        except Exception:
            print("Error: No values in queue")
            raise Exception

    def isEmpty(self):
        """
        checks to see if queue is empty
        Returns
        -------
            Boolean:
                True: queue is empty
                False: queue is not empty
        """
        if self.__head is None and self.__tail is None:
            return True
        else:
            return False


class Stack(object):
    """
    class that uses nodes to form a stack, a data structure where the First object in is the last object out.
    and the last object in is the first one out.
    ...

    Attributes
    ----------
    there are no attributes

    Methods
    -------
    __str__(self):
        Returns the data in queue as a string
    enqueue(self, newData):
        Adds an item to the end of the queue
    dequeue(self):
        Returns and removes the first item that was put into the queue
    isEmpty(self):
        Checks to see if the queue is empty and then returns a boolean
    """

    def __init__(self):
        """
        initiator function for the stack class
        """
        self.__top = None

    def __str__(self):
        """
        returns the data of the stack as an organized string
        Returns
        -------
            data_string (str): the stack data formatted as a string
        """
        # initiate some function vars
        data_string = ""
        i = True
        next_2_add = self.__top

        # checks to see if we have any values in stack or if there is only one item in stack before going to a loop
        if isinstance(next_2_add, Node):
            # if we have an top item, add it to the STR
            data_string = str(next_2_add.getData())
            # check to see if its alone, if so then we prevent the loop
            if isinstance(next_2_add.getNext(), Node):
                next_2_add = next_2_add.getNext()
            # prevents loop if the stack has 1 item
            else:
                i = False
        else:
            # prevents loop if the stack has no items
            i = False

        while i:
            # checks to see if the next value is the end of the stack
            # to be the the next Node if it exist
            if isinstance(next_2_add, Node):
                data_string += ", " + str(next_2_add.getData())
                next_2_add = next_2_add.getNext()
            # stops the loop if the next_2_add var is none indicating end of queue
            else:
                i = False
        data_string = "[" + data_string + "]"
        return data_string

    def push(self, newData):
        """
        adds an item to the top of the stack
        Parameters
        ----------
        newData: data to be added to the top of the stack

        Returns
        -------
        none, function is void

        """
        if self.__top is None:
            self.__top = Node(newData)
        else:
            self.__top = Node(newData, self.__top)

    def pop(self):
        """
        pops the top element from the stack
        Returns
        -------
        data_to_pop: the item at the top of the stack
        """
        if self.__top is None:
            return None
        data_2_pop = self.__top.getData()
        if self.__top.getNext() is None:
            self.__top = None
        else:
            self.__top = self.__top.getNext()
        return data_2_pop

    def isEmpty(self):
        """
        checks to see if the stack is empty
        Returns
        -------
            Boolean:
                True: stack empty
                False: stack has items
        """
        if self.__top is None:
            return True
        else:
            return False


def isPalindrome(s):
    """
    takes a string to determine if its a palindrome
    Parameters
    ----------
    s (str): string that we check to see is a palindrome

    Returns
    -------
    True/False boolean, True if the string is a palindrome, false is not
    """
    myStack = Stack()
    myQueue = Queue()
    # ensure input is a string and remove whirspace
    s = str(s).replace(" ", "").lower()
    # since queues and stacks are opposite in which item comes out first, we can add the full string to a stack and
    # queue and each char should be poped/dequeued in the same order if the words an palindrome
    for i in range(len(s)):
        myQueue.enqueue(s[i])
        myStack.push(s[i])
    for i in range(len(s)):
        if myStack.pop() != myQueue.dequeue():
            return False
    return True


def isPalindromeEC(s):
    """Implement if you wish to do the extra credit."""

    # Return appropriate value
    return
