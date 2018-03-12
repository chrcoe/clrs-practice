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
func (a *Array) Traverse() {
	for i, e := range a.array {
		fmt.Printf("index: %d element: %d\n", i, e)
	}
}

// Insert adds an element at the given index.
func (a *Array) Insert(value interface{}, index int) {
	a.array[index] = value
}

// Delete removes an element at the given index if the index is within the length of the array,
// otherwise it will throw an exception.
func (a *Array) Delete(index int) {
	a.array[index] = nil
}

// SearchByIndex returns the value of the element at the given index if it exists, or nil if it does
// not.
func (a *Array) SearchByIndex(index int) interface{} {
	return a.array[index] // this is using the builtin array with indexing .. I want to figure out how to add indexing to my own struct
}

// SearchByValue returns the index of the value if it exists, or nil if it does not.
func (a *Array) SearchByValue(value interface{}) int {
	for i, e := range a.array {
		if e == value {
			return i
		}
	}
	return -1
}

// Update will update an element at the given index.
func (a *Array) Update(value interface{}, index int) {
	a.array[index] = value
}

// Len returns the length of the array.
func (a *Array) Len() int {
	return a.len
}
