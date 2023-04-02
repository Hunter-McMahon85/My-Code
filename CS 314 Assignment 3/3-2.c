#include <stdio.h>
#include <stdlib.h>


/*

subq %rsi, %rdx 	# z -= y;

imulq %rdx, %rdi	# x *= z;

salq $63, %rdx  	# z = z << 63;

sarq $63, %rdx  	# z = z >> 63;

movq %rdi, %rax		# long ret_val = x;

orq %rdx, %rax  	# return ret_val | z;
ret 				# 

*/
// x = %rdi | y = %rsi | z = %rdx | %rax holds return value 
long 
f(long x, long y, long z){
	z -= y;
	x *= z;
	z = z << 63;
	z = z >> 63;
	long ret_val = x;
	return ret_val | z;
}

int 
  main()
{
	printf("f(1, 2, 4): %ld\n",f(1, 2, 4));
	printf("f(3, 5, 7): %ld\n",f(3, 5, 7));
	printf("f(10, 20, 40): %ld\n",f(10, 20, 40));
	printf("f(30, 50, 70): %ld\n",f(30, 50, 70));
	return 0;
}