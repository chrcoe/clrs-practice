/*
 * Main method which tests and shows the search functions working.
 */

#include <stdio.h>
#include <sort.h>

void print_array(int A[]);

int main()
{
	int myArray[5] = {5, 2, 25, 8, 10};
	int sizeof_a = sizeof(myArray) / sizeof(myArray[0]);
	printf("%d\n", sizeof_a);

	print_array(myArray);
	insertion_sort(myArray);
	print_array(myArray);



	return 0;
}

void print_array(int A[])
{
	int sizeof_a = sizeof(A);
	printf("{ ");
	for (int i = 0; i < sizeof_a; ++i)
	{
		//printf("value of i: %d\n", i);
		printf("%d ", A[i]);
	}
	printf("}\n");
}

