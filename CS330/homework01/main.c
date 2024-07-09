#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <dirent.h>
#include <errno.h>
#include <string.h>
#include <linux/limits.h>

void usage(int argc, char** argv);
void find_file(char* dir_name, char* file_to_find);

int main(int argc, char** argv)
{
	DIR* dp;
	struct dirent* dirp;

	// check if this application is being used properly
	usage(argc, argv);

	// check to see if provided directory is accessible
	errno = 0;
	dp = opendir(argv[1]);
	if(dp == NULL) {
		switch(errno) {
			case EACCES:
				fprintf(stderr, "Permission denied\n");
				break;
			case ENOENT:
				fprintf(stderr, "Directory does not exist\n");
				break;
			case ENOTDIR:
				fprintf(stderr, "'%s' is not a directory\n", argv[1]);
				break;	
		}
	}

	// print all files in the directory
	int cnt = 0;
	while((dirp = readdir(dp)) != NULL) {
		fprintf(stdout, "%d: %s", cnt, dirp->d_name);
		if(dirp->d_type == DT_DIR) {
			printf("\t directory");
		}
		printf("\n");
		cnt++;
	}

	// close the directory 
	closedir(dp);


	// now, recursivey traverse the directory structure to find the provided
	// file name
	char* file_to_find = argv[2];
	find_file(argv[1], file_to_find);

	return 0;
}


void usage(int argc, char** argv)
{
    if (argc != 3) {
        fprintf(stderr, "Usage: ./%s directory_name file_to_find\n", argv[0]);
        exit(EXIT_FAILURE);
    }
}

void
find_file(char* dir_name, char* file_to_find)
{	
	// we can achieve this function by taking the code from main and modifying it
	DIR* dp;
	dp = opendir(dir_name);
        struct dirent* dirp;

        // instead of printing files in a directory, we recurse if a give val is a dir
        while((dirp = readdir(dp)) != NULL)
       	{
		if(dirp->d_type == DT_DIR)
		{
			if ((strcmp(dirp->d_name, ".") != 0) &&  (strcmp(dirp->d_name, "..") != 0))
			{
			char subdir[strlen(dir_name)+2+strlen(dirp->d_name)];
			strcpy(subdir, dir_name);
			strcat(subdir, "/");
			strcat(subdir, dirp->d_name);
			find_file(subdir, file_to_find);
			}
		} 
		if (strcmp(dirp->d_name, file_to_find) == 0)
		{
				printf("Found %s in %s\n", file_to_find, dir_name);
		}		
        }
        // close the directory 
        closedir(dp);
}