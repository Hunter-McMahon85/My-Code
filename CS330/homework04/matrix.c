#include "matrix.h"

/* Debugging code that prints the BFS result for a particular iteration
   input parameters:
       int  rows	# of vertices
       int* color	array of color for the vertices
       int* distance	array of distance for the vertices
   return parameters:
       none
 */
void print_bfs_matrix_result(int rows, int* color, int* distance)
{
    assert(color);
    assert(distance);

    fprintf(stdout, "---- Print BFS Matrix Result ----\n");
    fprintf(stdout, "Vert\tCol\tDis\n");
    for(int i = 0; i < rows; i++) {
        fprintf(stdout, "%d\t%d\t%d\n", i, color[i], distance[i]);
    }
    fprintf(stdout, "--------\n\n");
}


/* Debugging code that prints a vector
   input parameters:
       int* vector	vector whose content we wish to print
       int  rows	# of elements in the vector
   return parameters:
       none
 */
void print_vector(int* vector, int rows)
{
    assert(vector);

    fprintf(stdout, "---- Print Vector ----\n");
    for(int i = 0; i < rows; i++) {
        fprintf(stdout, "%d\n", vector[i]);
    }
    fprintf(stdout, "--------\n\n");
}


/* Debugging code that prints the content of a 2D matrix
   input parameters:
       int* matrix	2D matrix we wish to print2D matrix we wish to print
       int  rows	# of rows of the input matrix
       int  cols	# of cols of the input matrix
   return parameters:
       none
 */
void print_matrix(int **matrix, int rows, int cols)
{
    assert(matrix);

    fprintf(stdout, "---- Print Matrix ----\n");
    fprintf(stdout, "This matrix is %d x %d\n", rows, cols);
    for(int i = 0; i < rows; i++) {
        for(int j = 0; j < cols; j++) {
            fprintf(stdout, "%d ", matrix[i][j]);
        }
        fprintf(stdout, "\n");
    }
    fprintf(stdout, "--------\n\n");

}


/* This function takes in a 2D matrix (src), transposes it and 
   then stores it in a destination 2D matrix (dst).
   Transpose operation takes each src[i][j] element and stores it
   in dst[j][i]
   
   input parameters:
       int** dst	Where you store the transpose of src
                        Dimensions are cols x rows
       int** src	Matrix you want to transpose
                        Dimensions are rows x cols
       int   rows	# of rows of input matrix (src)
       int   cols	# of cols of input matrix (src)
   return parameters:
       none
 */
void matrix_transpose(int** dst, int** src, int rows, int cols)
{
    	assert(dst);
    	assert(src);
    	assert(rows == cols);

	// INSERT YOUR CODE HERE
   	int i, j;
	// just need to flip indeicies i and j to transpose it
	for(i = 0; i < rows; i++)
	{
		for(j=0; j < cols; j++)
		{
			dst[i][j] = src[j][i];
		}
	}
}






/* This function 'resets a vetor to have all
   zero value
   input parameters:
       int* vector	the input vector to reset
       int  rows	the number of elements in the vector
   return parameters:
       none
 */
void reset_vector(int* vector, int rows)
{
    assert(vector);

    for(int i = 0; i < rows; i++) {
        vector[i] = 0;
    }
}
// two user def functions



/* This function calculates the sparse matrix-vector multiply from the matrix
   converted to COO format
   input parameters:
       these are 'consumed' by this function
       int**          int_array		2-d array of ints
       int            m			# of rows in the matrix
       int            n			# of columns in the matrix
       double         vector_x		input vector

       these are 'produced' by this function
       double*        res		Result of SpMV. res = A * x, where
                                        A is stored in CSR format and x is 
                                        stored in vector_x
   return parameters:
       none

 */
void
spmv(int** int_array, int m, int n, int* src, int* res)
{
	// convert to coo	
	int i, j;
	int nnz = 0;
	// find the # of non-zeros
	for (i=0; i<m; i++)
	{
		for(j=0; j<n; j++)
		{
			if(int_array[i][j] != 0)
			{
				nnz ++;
			}
		}
	}
	
	// allocate mem for the arrays
	int *coo_row_ind = (int*) malloc(nnz * sizeof(int));
    	int *coo_col_ind = (int*) malloc(nnz * sizeof(int));
    	int *coo_vals = (int*) malloc(nnz * sizeof(int));
	
	// loop through int_array and store stuff in the coo arrays
	int index = 0;
	for(i = 0; i<m; i++)
	{	
		for(j=0; j<n; j++)
		{
			if(int_array[i][j] != 0)
			{
				coo_row_ind[index] = i;
				coo_col_ind[index] = j;
				coo_vals[index] = int_array[i][j] ;
				index++;	
			}
		}
	}	

	// compute spmv
    	for(i=0; i<n; i++)
	{
		res[i] = 0;
	}

	for (int i=0; i<nnz; i++)
	{
		res[coo_row_ind[i]] += coo_vals[i] * src[coo_col_ind[i]];
	}
	//free the coo arrays:
	free(coo_row_ind);
	free(coo_col_ind);
	free(coo_vals);
}


/* SpMV-based BFS implementation
   input parameters:
   These are 'consumed' by this function
       int** int_array	input array representing the adjacency
                        matrix
       int   rows	# of rows of the adajcency matrix
       int   cols	# of cols of the adajcency matrix
       int   source	source vertex for the BFS
   These are 'produced' by this function
       int*  color	color array
       int*  distance	distance array
   return parameters:
       none
  */
void
bfs_spmv(int** int_array, int rows, int cols, int source, int* color, int* distance)
{
    	// check the input parameters to see if they are valid
    	if(rows != cols) {
        	fprintf(stderr, "Not an adjacency matrix\n");
		exit(EXIT_FAILURE);
    	}	
    	if(source >= rows) {
        	fprintf(stderr, "Invalid source vertex\n");
		exit(EXIT_FAILURE);
    	}
    	assert(int_array);
    	assert(color);
    	assert(distance);

    	fprintf(stdout, "Breadth first search on the graph using SpMV ... ");

    	// Transpose the adjacency matrix
    	int** mat_trans = NULL;
    	init_2d_array(&mat_trans, cols, rows);
    	matrix_transpose(mat_trans, int_array, rows, cols);
    	#if DEBUG
        	print_matrix(mat_trans, cols, rows);
    	#endif
    	// Initialize the various data structures
    	int* vec = (int*) malloc(sizeof(int) * rows);
    	assert(vec);
    	for(int i = 0; i < rows; i++) {
        	if(i == source) {
            		vec[i] = 1;
           		color[i] = 2;
            		distance[i] = 0;
        	} else {
            		vec[i] = 0;
            		color[i] = 0;
            		distance[i] = -1;
        	}
    	}
    	int* res = (int*) malloc(sizeof(int) * cols);
    	assert(res);
    	reset_vector(res, cols);


    	int iter = 1;
    	int done = 0;
    	int *src = vec;
    	int *dst = res;

    	// Do BFS until done
    	while(!done) {
        	// INSERT YOUR CODE HERE
		int i, j;
        	// given a vector of source vetices, find the neighbors HINT: spmv
		spmv(int_array, rows, cols, src, dst);

        	// store the distance for the newly discovered neighbors
        	// color the source vertices for this iteration `black'
		for(i=0; i<rows; i++)
		{
			if((dst[i] > 0) && (color[i] == 0))
			{
				color[i] = 2;
				distance[i] = iter;
			}
		}
		
        	// eliminate vistied row vals from nodes weve visited
        	for(i = 0; i<rows; i++)
		{	
			if(color[i] == 2)
			{
				for(j=0; j<cols; j++)
				{
					int_array[i][j] = 0;
				}
			}

		}

		// Check to see if no neighbors were found, in which case, we are done
		int same = 1;
       		for (int i = 0; i < rows; i++) 
		{
            		if (dst[i] != src[i]) 
			{
                		same = 0;
                		break;
            		}	
        	}
        	if (same)
	       	{
            		done = 1;
        	}
		// ensures we dont overite one or the other unintentionally in spmv		
		int* tmp = src;	
		src = dst;
		dst = tmp;

		// iter is equivalent to each `breadth' searched (i.e., distance from the source vertex)
		iter++;
    	}

    	fprintf(stdout, "done\n");

   	#if DEBUG
        	print_bfs_matrix_result(rows, color, distance);
   	#endif

    	free_2d_array(mat_trans, cols);
    	free(vec);
    	free(res);
}


/* This function allocates memory for a 2D array of size rows x cols
   input parameters
       int*** arr		reference to the 2D array you want to init
       int    rows		# of rows in the 2D array
       int    cols		# of columns in the 2D array
   return parameters:
        none
 */
void init_2d_array(int*** arr, int rows, int cols)
{
    int** tmpArr = (int**) malloc(sizeof(int*) * rows);
    assert(tmpArr);
    for(int i = 0; i < rows; i++) {
        tmpArr[i] = (int*) malloc(sizeof(int) * cols);
        assert(tmpArr[i]);
    }
    *arr = tmpArr;

}


/* This function frees memory allocated to a 2D array.
   input parameters:
       int** arr	the 2D array to deallocate
       int   rows	# of rows of the matrix
   return parameters:
       none
 */
void free_2d_array(int** arr, int rows)
{
    for(int i = 0; i < rows; i++) {
        // free each row
        free(arr[i]);
    }
    // free the matrix
    free(arr);
}
