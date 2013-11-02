#include <unistd.h>
#include <stdio.h>

int main()
{
	int i;
	for ( i = 0 ; i < 100; i++) {
		printf("Sleeping...\n");
		sleep(42);
	}
	printf("Done!\n");
	return 0;
}
