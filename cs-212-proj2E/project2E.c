#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* in the event of a failure */
void IssueBadFileError(char *bad_name){
printf(" <%s> is not a valid file.\n", bad_name);
	exit(EXIT_FAILURE);
}


void word_instances(char *text, char *first_char, int word_length,int *counter_ptr){
    /* take the word to search for, find where it exist in the text and update the counter acordingly*/
    
	/* we need some constants to store some values*/
    int char_count = strlen(text);
    
    /* keeps track of our matches */
    int num_o_matches = 0;
    
    /*we need to know how long the current word is, this var stores that and is reset
     each time there is a word seperator*/
    int length = 0;
    
    /* for the loop iteration, loop goes from char to char*/
    int iter = 0;
    int i = 1;
    
    while (i == 1){
        if (iter == char_count){
            i = 0;
        }
        /* get the ascii value of the current char */
        int word_num = text[iter];
        int check_match = 0;
        
        /* if the char is not an alphanumeric char and is /n , . ' ' 
         *thus signaling the end of the word meaning its time to check if we have a match
         */
        switch(word_num){
            case 10:
                check_match = 1;
                break;
            case 32:
                check_match = 1;
                break;
            case 44:
                check_match = 1;
                break;
            case 46:
                check_match = 1;
                break;
            default:
                length ++;
        }
        /* loop throught the current word char by char to see if it equals the given word 
            we do this by using the length of the current word to determine where to start and end
         */
        int iter2= 0;
        int x = 1;
        if (check_match == 1){
            /* makes it such that the code only checks sutiable canidates 
             *in words that are the same length*/
            if (length == word_length) {
                    int letter_match = 0;
                    while(x==1){
                        if (iter2+1 == length){
                            x = 0;
                        }
                        if (text[iter - length + iter2] != first_char[iter2]){
                            x=0;
                            break;
                        } else { 
                            letter_match += 1;
                        }
                        iter2++;
                    }
                    if (letter_match == word_length){
                        num_o_matches++;
                    }
                }
                length = 0;
        }
        iter++;
    }
     /* set the counter_ptr to have its value equal to the num_o_matches */
    *counter_ptr = num_o_matches;
}

/* for printing out our funciton latter */
void display_count(char *word, int count){
	printf("The word \"%s\" occurs %d times.\n", word, count);
}

int main(int argc, char *argv[]){
	int args_index = argc - 3;
/* read the file and store its contents to memory with malloc -done */
	FILE *raw_file = fopen(argv[1],"r");
	if(raw_file == NULL){
		IssueBadFileError(argv[1]);
		return 1;
	}
	fseek(raw_file, 0 ,SEEK_END);
	int file_size = ftell(raw_file);
	char *txt_file = malloc(file_size+1);
	fseek(raw_file, 0, SEEK_SET);
	fread(txt_file, 1, file_size, raw_file);
	fclose(raw_file);

/* reserve memory for the counters -done */
	int *counters = malloc((argc-2)*4);

/* call word_instances to put the # of occurances of each word in the proper counter*/
	int i = 0;
    int iterate = 1;
    while( iterate == 1){
    if (i == args_index){
        iterate = 0;
    }
    counters[i] = 0;
    word_instances(txt_file, argv[i+2], strlen(argv[i+2]),&counters[i]);
    i++;
	}


/*print results*/
    int j = 0;
    int iterator = 1;
    while (iterator == 1 ){
        if (j == argc-3){
            iterator = 0;
        }
        display_count(argv[2+j], counters[j]);
        j++;
    }

/* free memory and return zero to indicate a success */
	free(counters);
	free(txt_file);
	return 0;
}
