This project was meant to be practice for using pointers and working with arrays.

it has a few parts

int * AllocateArray(int N) - generates an random array of N elements and returns a memory pointer to where the created array starts
void SortArray(int *A, int N) - sorts array starting at pointer A with N elements from greatest to least
void DeallocateArray(int *A) - frees the memory for a given array A
int Main() - takes a list of some integers, then loops through that list, allocating an array of the size of each int, sorts it, then deallocates it before printing off the real world time it took to do each operation


docstrings were not required on this assigment and most comments in this case are instructions on what to do.
Additionally, unittest with c was something not covered in this course and for each assignment,
the instructor provided a checker bash script to check for correctness. 
