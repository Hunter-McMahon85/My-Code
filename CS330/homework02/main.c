#include <stdlib.h>
#include <stdio.h>
#include "main.h"

/* Since the largest number is 4294967295, we need 11 characters (including the 
   null character) to read a number from the file */
#define MAX_NUM_LENGTH 12


/* This function checks the number of input parameters to the program to make 
   sure it is correct. If the number of input parameters is incorrect, it 
   prints out a message on how to properly use the program.
   input parameters:
       int    argc
       char** argv 
    return parameters:
       none
 */
void
usage(int argc, char** argv)
{
    if(argc < 4) {
        fprintf(stderr, 
               "usage: %s <input file 1> <input file 2> <output file>\n", 
                argv[0]);
        exit(EXIT_FAILURE);
    }
}


/* This function takes in the two input file names (stored in argv) and
   determines the number of integers in each file.
   If the two files both have N integers, return N, otherwise return -1.
   If one or both of the files do not exist, it should exit with EXIT_FAILURE.
   input parameters:
       char** argv
   return parameters:
       -1 if the two input files have different number of integers 
       N  if the two input files both have N integers
 */
int
get_num_ints(char** argv)
{
	// est file ptrs and open files 
	FILE *fp1 = NULL;
	FILE *fp2 = NULL;
	fp1 = fopen(argv[1],"r"); 
	fp2 = fopen(argv[2],"r");
	// make sure the files exist
        if((fp1 == NULL) || (fp2 == NULL)) 
	{
       		printf("Error, one or both input files does not exist\n");
        	exit(EXIT_FAILURE);
	}
	// count the # lines in each
	int f1_count = 0;
	int f2_count = 0;
	int num_holder;
	// refered to tutorialspoint.com/c-program-to-count-the-number-of-lines-in-a-file
	// and 
	// refered to tutorialspoint.com/c_standard_library/c_function_sscanf.htm
	while(fscanf(fp1, "%u", &num_holder) == 1)
	{
		f1_count ++;
	}
	while(fscanf(fp2, "%u", &num_holder) == 1)
	{
		f2_count ++;
	}
	fclose(fp1);
	fclose(fp2);
	// printf("%d %d \n", f1_count, f2_count);
	// returns
	// make sure theyre the same
	if (f1_count - f2_count != 0)
	{
		// if not the same... to the shadow realm
		return -1;
	}
	return f1_count;
}


/* This function allocates engough memory to the three arrays to store
   num_ints elements each.
   This function should exit with EXIT_FAILURE if the program fails to allocate
   the memory.
   input parameters:
       unsigned int*      input_one
       unsigned int*      input_two
       unsigned long int* output
       int                num_ints
   return parameters:
       none
 */
void
allocate_mem(unsigned int** input_one, unsigned int** input_two, unsigned long int** output, int num_ints)
{
	// reserve mem 4 inputs and outputs
	// input 1
	int list_size = num_ints * sizeof(unsigned int); 
	*input_one = malloc(list_size);	
        // if input 1 fails
        if(*input_one == NULL) 
	{
       		printf("Error, could not alloc input 1\n");
        	exit(EXIT_FAILURE);
	}
	// input 2
	*input_two = malloc(list_size);
        // if 2 fails
        if(*input_two == NULL) 
	{
       		printf("Error, could not alloc input 2\n");
		free(input_one);
        	exit(EXIT_FAILURE);
	}
	// output
	*output = malloc(num_ints * sizeof(unsigned long int));
        // if output fails
	if(*output == NULL) 
	{
       		printf("Error, could not malloc output\n");
		free(input_one);
		free(input_two);
        	exit(EXIT_FAILURE);
	}
}



/* This function reads in num_ints integers from the two input files and 
   stores them in input_one (first input file) and input_two (second input
   file).
   If one or both of the files do not exist, it should exit with EXIT_FAILURE.
   input parameters:
       char**        argv
       unsigned int* input_one
       unsigned int* input_two
       int           num_ints
   return parameters:
       none

 */
void
get_ints(char** argv, unsigned int* input_one, unsigned int* input_two, unsigned long int* output, int num_ints)
{
	// est file pointers and open them
	FILE *fp1 = NULL;
	FILE *fp2 = NULL;
	fp1 = fopen(argv[1],"r"); 
	fp2 = fopen(argv[2],"r");
	// make sure the files exist
        if((fp1 == NULL) || (fp2 == NULL)) 
	{
       		printf("Error, one or both input files does not exist\n");
        	exit(EXIT_FAILURE);
	}
	// get the ints from the file 
	int i;
	char holder1[MAX_NUM_LENGTH];
	char holder2[MAX_NUM_LENGTH];
	for(i = 0; i < num_ints; i++)
	{	
		fgets(holder1, MAX_NUM_LENGTH, fp1);
		fgets(holder2, MAX_NUM_LENGTH, fp2);
		// fgets only gets them as strings, sscanf ensures their unsigned ints
		sscanf(holder1, "%u", &input_one[i]);
		sscanf(holder2, "%u", &input_two[i]);
	}
	fclose(fp1);
	fclose(fp2);
}

/* This function does an element-wise addition between the two input arrays 
   (input_one and input_two) of size num_ints and stores the result in the 
   output array (output).
   input parameters:
       unsigned int*      intput_one
       unsigned int*      intput_two
       unsigned long int* output
       int                num_ints
   return parameters:
       none
 */
void
sum_ints(unsigned int* input_one, unsigned int* input_two, unsigned long int* output, int num_ints)
{
  /* done, just loops through and sums values */
	for(int i=0; i<num_ints; i++)
	{
		output[i] = input_one[i] + input_two[i]; 
	}
}

/* This function saves the summed output to an output file, whose name was 
   specified with the program execution (i.e., argv[3]).
   The file should containe one integer value per line, similarly to how the
   input files were stored.
   input parameters:
       char**             argv
       unsigned int*      intput_one
       unsigned int*      intput_two
       unsigned long int* output
       int                num_ints
   return parameters:
       none
 */
void
save_output(char** argv, unsigned int* input_one, unsigned int* input_two, unsigned long int* output, int num_ints)
{
	/* done */
	// create/open output file
	FILE *fp;
	fp = fopen(argv[3], "w");
	// write to output file
	int i;
	for(i=0; i<num_ints; i++)
	{	
		// holder is just an alias for each value thats then writen to the file
		// by fputs
		char holder[MAX_NUM_LENGTH];
		sprintf(holder, "%lu", output[i]);
		fputs(holder, fp);
		fputs("\n", fp);
	}
	fclose(fp);
}

/* This program takes in three text file names as input. 
   The first two files contain N integers (where N >=0 and N <= 1,000,000)
   whose values range from 0 to 4294967295 (i.e., 32-bit unsigned integers).
   The last file is the output file that this program should generate.
   For all three files, there should be one integer per line.
  
   For each line in the two input files, read in the two integers, add them, and
   then store the sum in the output file.
   Repeat this process until all integers have been read from the input files.

   For example, if the two input files have eight integerse each
   input file 1		input file 2		output file
   --------------------------------------------------------
   1			2			3
   5			2			7
   8			5			13
   1			12			13
   2			2			4
   10			2			12
   1991			2			1993
   11231245		21235			11252480
 */
int
main(int argc, char** argv)
{
    usage(argc, argv);

    // Check the number of integers in the input files
    int num_ints = get_num_ints(argv);
    if(num_ints == -1) {
        fprintf(stderr, "ERR: The two input files have different # of ints\n");
        exit(EXIT_FAILURE);
    } 

    unsigned int* input_one = NULL;
    unsigned int* input_two = NULL;
    unsigned long int* output = NULL;
    // Allocate memory to store the integers
    allocate_mem(&input_one, &input_two, &output, num_ints);

    // Read the integers from the two input files
    get_ints(argv, input_one, input_two, output, num_ints);
   
    // Sum up the numbers
    sum_ints(input_one, input_two, output, num_ints);

    // Store the result in the output file 
    save_output(argv, input_one, input_two, output, num_ints);

    free(input_one);
    free(input_two);
    free(output);

    return 0;
}
