package array

import "fmt"

// Array implements an array attempting to not use any built in arrays.  Kind of silly, but it is a
// starting point for the rest of the code-kata.  Unfortunately I cannot seem to find any other way
// to create a manual array by allocating memory blocks etc ..
type Array struct {
	array []interface{}
	len   int // how large do we want to make this ?
}

// New provides a new array.
func New(elemType interface{}, len int) *Array {
	t := make([]interface{}, len)
	return &Array{t, len}
}

// Traverse will print out all of the elements in the array one by one.
// This should end up being O(1) and Ω(1)
func (a *Array) Traverse() {
	for i, e := range a.array {
		fmt.Printf("index: %d element: %d\n", i, e)
	}
}

// Insert adds an element at the given index.  This always overwrites whatever is already at the
// index and does not do any element shifting.  This is not really what we want...
// This should end up being O(n) and Ω(1)
func (a *Array) Insert(value interface{}, index int) {
	// TODO: need to shift all elements after this element ++
	// if the array is already at max capacity (index >= len) then we need to grow the array before
	// inserting.

	if index >= a.len {
		a.grow()
	}

	j, n := a.len, a.len
	n += 1

	for j >= index {
		if a.array[j+1] != nil {
			a.array[j+1] = a.array[j]
		}
		j -= 1
	}
	a.array[index] = value

}

// grow will grow the internal array
func (a *Array) grow() {
	growthMultiplier := 2
	fmt.Printf("growing the array by multiplying by a factor of %d\n", growthMultiplier)
	newArray := make([]interface{}, a.len*growthMultiplier)
	for i, e := range a.array {
		newArray[i] = e
	}
	a.array = newArray
	a.len = a.len * growthMultiplier
}

// Delete removes an element at the given index if the index is within the length of the array,
// otherwise it will throw an exception.  This will shift items with an index greater than the index
// deleted.
// This should end up being O(n) and Ω(1)
func (a *Array) Delete(index int) {
	a.array[index] = nil
}

// SearchByIndex returns the value of the element at the given index if it exists, or nil if it does
// not.
// This should be O(1) and Ω(1)
func (a *Array) SearchByIndex(index int) interface{} {
	return a.array[index] // this is using the builtin array with indexing .. I want to figure out how to add indexing to my own struct
}

// SearchByValue returns the index of the value if it exists, or nil if it does not.
// This should be O(n) and Ω(1)
func (a *Array) SearchByValue(value interface{}) int {
	for i, e := range a.array {
		if e == value {
			return i
		}
	}
	return -1 // REFACTOR: should I be returning -1 here ? doesn't seem normal ..
}

// Update will update an element at the given index.
// This should be O(1) and Ω(1)
func (a *Array) Update(value interface{}, index int) {
	a.array[index] = value
}

// Len returns the length of the array.
// This should be O(1) and Ω(1)
func (a *Array) Len() int {
	return a.len
}
