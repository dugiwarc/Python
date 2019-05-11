#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() 
{
	float input;
	printf("Enter grade for Math Elem: ");
	scanf("%f", &input);
	input *= 0.6;
	printf("%f", input);

	return 0;
}