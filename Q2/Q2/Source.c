#include <stdio.h>

#define MIN		1
#define MAXINDEX	10
#define MAXTABLE	10
#define STEP		1

void main(void)
{
	int i, j;

	for (j = MIN; j < MAXTABLE; j += STEP) {
		for (i = MIN; i <= MAXINDEX; i += STEP)
			printf(" %3d * %3d = % 3d\n", i, j, i * j);
	printf("\n---------------\n\n");
	}

	for (i = MIN; i <= MAXINDEX; i += STEP)
		printf(" % 3d * %3d = % 3d\n", i, MAXTABLE, i * MAXTABLE);
}