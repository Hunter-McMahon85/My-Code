#include <stdio.h>
#include <stdlib.h>

struct 
IntArray{
	int length;
	int *dataptr;
};

struct IntArray* 
mallocintArray(int length){
	struct IntArray* new_int_array = malloc(sizeof(struct IntArray));
	new_int_array->length = length;
	new_int_array->dataptr = malloc(sizeof(int)*length);
	return new_int_array;
}

void
freeIntArray(struct IntArray * arrayptr){
	free(arrayptr->dataptr);
	free(arrayptr);
}



int 
readInt() {
	// modified helper function from lab 4 code, this one is used to get
	// the user input for length
    char lineBuf[10];
    char *p = NULL;
    int n;

    while (1) {
        // char* fgets (char* str, int num, FILE* stream);
        fgets(lineBuf, sizeof(lineBuf), stdin);

        // long int strtol (const char* str, char** endptr, int base);
        n = strtol(lineBuf, &p, 10);
        // this conditional is the only thing that needed to be modified
        if ((lineBuf != p) && (n != 0)) {
            break;
        }
        printf("Invalid input\n");
        break;
    }
    return n;
}

void
readIntArray(struct IntArray * array){
		char lineBuf[10];
        char *p = NULL;
        int n;
        int i = 0;
		do{
			printf("Enter int: ");
    		while (1) {
                // again we can modify the readint function given in lab4

                fgets(lineBuf, sizeof(lineBuf), stdin);
                n = strtol(lineBuf, &p, 10);
                if (lineBuf != p) {
                	array->dataptr[i] = n;
            		i ++;
                    break;
                }
                printf("Invalid input\n");
                break;
        	}
        	// and create a nested while loop
    	} while(i < array->length); 
}
       

void
swap(int *xp, int *yp) {
	int hold_this = *xp;
	*xp = *yp;
	*yp = hold_this;
}

void
sortIntArray(struct IntArray *array){
	// i refered to https://geeksforgeeks.org/bubble-sort/ on this
	for (int i = 0; i < array->length-1; i++){

		for (int j = 0; j < array->length - i - 1; j++){

			if (array->dataptr[j] > array->dataptr[j+1]){
				swap(&array->dataptr[j], &array->dataptr[j+1]);
			}
		}
	}
}

void
printIntArray(struct IntArray *array){
	printf("[ %d", array->dataptr[0]);
	for (int i = 1; i < array->length; i++){
		printf(", %d", array->dataptr[i]);
	}
	printf(" ]\n");
}

int 
main(){
	int length = 0;
	do{
		printf("Enter length: ");
    	length = readInt();
    } while(length == 0); 

    struct IntArray * user_array = mallocintArray(length);
    readIntArray(user_array);
    sortIntArray(user_array);
    printIntArray(user_array); 
    freeIntArray(user_array);
	return 0;
}
