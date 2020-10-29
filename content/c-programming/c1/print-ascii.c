#include <stdio.h>

main(){

	int i = 0;
	char c = 0;

	while (i <= 127){

		printf("%d\t\"%c\"\n", i, c);

		c = c + 1;
		i = i + 1;
	}
}
