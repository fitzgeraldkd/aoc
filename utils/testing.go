package utils

import (
	"reflect"
	"testing"
)

func AssertEqual[T string | int](t *testing.T, answer T, expected T) {
	if answer != expected {
		t.Error("\nReceived:", answer, "\nExpected:", expected)
	}
}

func AssertListEqual[T []string | []int](t *testing.T, answer T, expected T) {
	if !reflect.DeepEqual(answer, expected) {
		t.Error("\nReceived:", answer, "\nExpected:", expected)
	}
}
