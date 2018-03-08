package array

import "fmt"

// Array implements an array attempting to not use any built in arrays.  Kind of silly, but it is a
// starting point for the rest of the code-kata.
type Array struct {
	array []interface{}
	len   int // how large do we want to make this ?
}

// New provides a new array.
func New(elemType interface{}, len int) *Array {
	// https://stackoverflow.com/questions/30716354/how-do-i-do-a-literal-int64-in-go
	//
	fmt.Println(elemType)
	t := make([]interface{}, len)
	return &Array{t, len}
}

// Traverse will print out all of the elements in the array one by one.
func (a *Array) Traverse() {
}

// Insert adds an element at the given index.
func (a *Array) Insert(value interface{}, index int) {
	a.array[index] = value
}

// Delete removes an element at the given index if the index is within the length of the array,
// otherwise it will throw an exception.
func (a *Array) Delete(index int) {
}

// SearchByIndex returns the value of the element at the given index if it exists, or nil if it does
// not.
func (a *Array) SearchByIndex(index int) interface{} {
	return a.array[index] // this is using the builtin array with indexing .. I want to figure out how to add indexing to my own struct
}

// SearchByValue returns the index of the value if it exists, or nil if it does not.
func (a *Array) SearchByValue(value interface{}) interface{} {
	return nil
}

// Update will update an element at the given index.
func (a *Array) Update(index int) {
}

// Len returns the length of the array.
func (a *Array) Len() int {
	return a.len
}
