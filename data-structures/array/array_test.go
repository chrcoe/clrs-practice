package array

import (
	"go/types"
	"testing"
)

func TestNew(t *testing.T) {
	// fill out the tests here ..
	a := New(types.String, 10)

	if a.Len() != 10 {
		t.Error()
	}

	a.Insert("test", 2)
	if a.SearchByIndex(2) != "test" {
		t.Error()
	}
}
