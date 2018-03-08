#include <stdio.h>
#include <sort.h>

int insertion_sort(int A[])
{
	printf("insertion sort not implemented yet!\n");

	int sizeof_a = sizeof(A);

	for ( int i = 1; i < sizeof_a; ++i)
	{
		int current_key = A[i];
		int index = i - 1;

		while (index >= 0 && A[index] > current_key)
		{
			swap(&index, &index + 1);
			index -= 1;
		}
		A[index + 1] = current_key;
	}
}

void swap(int *x, int *y)
{
	// to use, need pointers: swap (&a, &b)
	int temp;
	temp = *x;
	*x = *y;
	*y = temp;

	return;
}
