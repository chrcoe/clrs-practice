int binary_search_iter(int A[], int v, int low, int high)
{
	/*
	 * Takes in a pre-sorted array, an item to search for and a range to search for.
	 *
	 * Uses an iterative approach.
	 *
	 * This algorithm runs in O(log(n)) because it is cutting down the search scope
	 * by half each time through the loop.
	 *
	 */
	while (low <= high)
	{
		int mid = (low + high) / 2;
		if (v == A[mid])
		{
			return mid;
		}
		else if (v > A[mid])
		{
			low = mid + 1;
		}
		else high = mid + 1;
	}

	return -1;
}


int binary_search_recurs(int A[], int v, int low, int high)
{
	/*
	 * Takes in a pre-sorted array, an item to search for and a range to search for.
	 *
	 * Uses a recursive approach.
	 *
	 * This algorithm runs in O(log(n)) because it is cutting down the search scope
	 * by half each time through the loop.
	 *
	 */
	if (low > high)
	{
		// first stopping condition
		return -1;
	}

	int mid = (low + high) / 2;
	if (v == A[mid])
	{
		// second stopping condition
		return mid;
	}
	else if (v > A[mid])
	{
		return binary_search_recurs(A, v, mid + 1, high);
	}
	else
	{
		return binary_search_recurs(A, v, low, mid - 1);
	}
}
