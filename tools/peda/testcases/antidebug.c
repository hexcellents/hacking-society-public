#include <stdlib.h>
#include <stdio.h>
#include <sys/ptrace.h>

int main()
{
	printf("Checking if I'm run under a debugger...\n");
	if(ptrace(PTRACE_TRACEME, 0, 0, 0) < 0) {
		printf("Yup\n");
		exit(0);
	}

	printf("Nope, doesn't seem like it!\n");
	return 0;
}
