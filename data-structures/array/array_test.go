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

	if a.array == nil {
		t.Error()
	}
	// how to test traversal - this isn't providing an iterator directly ..
	// a.Traverse()

}

func TestInsert(t *testing.T) {
	a := New(types.String, 10)

	// for i := 0; i < a.Len(); i++ {
	// 	a.Update(i*2, i)
	// }
	a.Traverse()
	a.Insert("test", 2)
	// 	if a.SearchByIndex(2) != "test" {
	// 		t.Error()
	// 	}
	a.Traverse()
}

func TestDelete(t *testing.T) {
	a := New(types.String, 10)
	a.Insert("test", 2)
	a.Delete(2)
	if a.SearchByIndex(2) != nil {
		t.Error()
	}
}

func TestSearchByIndex(t *testing.T) {
	a := New(types.String, 10)
	for i := 0; i < a.Len(); i++ {
		if a.SearchByIndex(i) != nil {
			t.Error()
		}
	}

	a.Insert("test", 2)
	if a.SearchByIndex(2) != "test" {
		t.Error()
	}
}

func TestSearchByValue(t *testing.T) {
	a := New(types.String, 10)
	if a.SearchByValue("test") != -1 {
		t.Error()
	}

	a.Insert("test", 3)
	if a.SearchByValue("test") != 3 {
		t.Error()
	}
}

func TestUpdate(t *testing.T) {
	a := New(types.String, 10)
	if a.SearchByIndex(2) != nil {
		t.Error()
	}

	a.Update("test", 2)
	if a.SearchByIndex(2) != "test" {
		t.Error()
	}

}
