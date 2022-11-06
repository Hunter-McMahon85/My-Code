#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>


int *AllocateArray(int N)
{
	/* 
	* Allocate an array with N integers.
	* The value of each element of the array should be a
	* random number between 0 and 10N.
	* Hint: use the rand() function and a modulo operator.
	*/
	int * array = malloc(sizeof(int)*N);
	for (int i = 0; i <= N; i++){
		array[i] = rand() % (10*N+1);
	}
	return array;
}

void SortArray(int *A, int N)
{
	for(int i = 0; i <= N; i++){
		for(int j = i+1; j <=N; j++){
			if(A[j] < A[i]){
				int placeholder = A[i];
				A[i] = A[j];
				A[j] = placeholder;
					} 
			}		
    }
    /* PRINT IT
   	 for(int i = 1; i < N; i++){
       		 if (i%10 != 0){
        		printf("\t%d", A[i]);
        	} else {
           		printf("\t%d\n", A[i]); 
        	}	
    	}*/
    }

void DeallocateArray(int *A)
{
	free(A); 
}

int main()
{
    int sizes[8] = { 1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000 };

/* 
 *  For fun:
 *  int sizes[11] = { 1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000,
 *                    256000, 512000, 1024000 }; 
 */

    for (int i = 0 ; i < 8 ; i++)
    {
        double alloc_time = 0., sort_time = 0., dealloc_time = 0.;
        struct timeval startTime;
        struct timeval endTime;

        /* 
	 * Call the three functions in a sequence. Also use
         * gettimeofday calls surrounding each function and set the 
         * corresponding variable (alloc_time, sort_time, dealloc_time).
         */
        
        gettimeofday(&startTime, 0);
        int * current_array = AllocateArray(sizes[i]);
        gettimeofday(&endTime, 0);
        alloc_time = (endTime.tv_sec-startTime.tv_sec)+(endTime.tv_usec-startTime.tv_usec)/1000000.;
        
        gettimeofday(&startTime, 0);
        SortArray(current_array, sizes[i]);
        gettimeofday(&endTime, 0);
        sort_time = (endTime.tv_sec-startTime.tv_sec)+(endTime.tv_usec-startTime.tv_usec)/1000000.;
        
        gettimeofday(&startTime, 00);
        DeallocateArray(current_array);
        gettimeofday(&endTime, 0);
        dealloc_time = (endTime.tv_sec-startTime.tv_sec)+(endTime.tv_usec-startTime.tv_usec)/1000000.;

        printf("Timings for array of size %d\n", sizes[i]);
        printf("\tTime for allocation is %g, time per element = %g\n", alloc_time, alloc_time/sizes[i]);
        printf("\tTime for sort_time is %g, time per element = %g\n", sort_time, sort_time/sizes[i]);
        printf("\tTime for deallocation is %g\n", dealloc_time);
    }
}
