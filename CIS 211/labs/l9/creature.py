"""
Hunter McMahon
CIS 211
lab 9
"""

from time import sleep, perf_counter
from threading import Thread


# pt1, some tree data structure/recursion practice
# the abstract class
class Creature(object):

    def __init__(self):
        raise NotImplementedError("Abstract classes should not be instantiated")

    def __str__(self) -> str:
        raise NotImplementedError("Abstract class methods should not be called")

    def search(self, value: str) -> bool:
        raise NotImplementedError("Abstract class methods should not be called")


class Head(Creature):
    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return self.name

    def search(self, value: str) -> bool:
        if value == self.name:
            return True
        return False


class Orthrus(Creature):
    def __init__(self, left_head: Head, right_head: Head):
        """
        initiator for orthrus
        :param left_head: instance of head
        :param right_head: instance of head
        """
        self.left = left_head
        self.right = right_head

    def __str__(self) -> str:
        return f'({self.left} {self.right})'

    def search(self, value: str) -> bool:
        if self.left.search(value) or self.right.search(value):
            return True
        return False


class Cerberus(Creature):
    def __init__(self, left_head, mid_head, right_head):
        """
        initiator for the cerberus class
        :param left_head: instance of Head or Orthrus
        :param mid_head: instance of Head or Orthrus
        :param right_head: instance of Head or Orthrus
        """
        self.left = left_head
        self.middle = mid_head
        self.right = right_head

    def __str__(self) -> str:
        return f'[{self.left} {self.middle} {self.right}]'

    def search(self, value: str) -> bool:
        if self.left.search(value) or self.right.search(value) or self.middle.search(value):
            return True
        return False


# pt2, multi-threaded code practice
# follows instructions on https://www.pythontutorial.net/advanced-python/python-threading/

# ie a simple single threaded program
def task():
    """
    just does something over 1 second
    """
    print('Starting a task...')
    sleep(1)
    print('done')


# starts a timer
start_time = perf_counter()

# takes up 2 seconds of time
task()
task()

# ends a timer
end_time = perf_counter()

print(f'It took {end_time - start_time: 0.1f} second(s) to complete.')

# now for a multi threaded example w/ the threading module:

# new_thread = Thread(target=fn,args=args_tuple)
# target: specifies a function (fn) to run in the new thread.
# args: specifies the arguments of the function (fn). The args argument is a tuple.

start_time = perf_counter()

# create two new threads
t1 = Thread(target=task)
t2 = Thread(target=task)

# start the threads
t1.start()
t2.start()

# wait for the threads to complete
t1.join()
t2.join()

end_time = perf_counter()

print(f'It took {end_time - start_time: 0.1f} second(s) to complete.')

