/*
 * Main method which tests and shows the search functions working.
 */


#include "stdio.h"
#include "search.h"

int main()
{
	int myArray[5] = {1, 2, 5, 8, 10};
	int sizeof_a = sizeof(myArray) / sizeof(myArray[0]);

	int wanted_item = 8;

	int index = binary_search_iter(myArray, wanted_item, 0, sizeof_a - 1);
	printf("Location of %d (expecting 3):\t %d\n", wanted_item, index);

	wanted_item = 10;
	index = binary_search_recurs(myArray, wanted_item, 0, sizeof_a - 1);
	printf("Location of %d (expecting 4):\t %d\n", wanted_item, index);


	wanted_item = 25;
	index = binary_search_recurs(myArray, wanted_item, 0, sizeof_a - 1);
	printf("Location of %d (expecting -1):\t %d\n", wanted_item, index);

	return 0;
}
