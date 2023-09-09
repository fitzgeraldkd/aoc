package aoc_2019_04

import (
	"testing"

	utils "github.com/fitzgeraldkd/aoc/utils"
)

func TestPart1(t *testing.T) {
	utils.AssertEqual(t, Part1(""), 1653)
}

func TestPart2(t *testing.T) {
	utils.AssertEqual(t, Part2(""), 1133)
}

func TestUtils(t *testing.T) {
	utils.AssertFalse(t, hasDouble([6]int{1, 2, 3, 4, 5, 6}, false))
	utils.AssertFalse(t, hasDouble([6]int{1, 2, 3, 1, 3, 6}, false))
	utils.AssertTrue(t, hasDouble([6]int{1, 1, 3, 4, 5, 6}, false))
	utils.AssertTrue(t, hasDouble([6]int{1, 2, 3, 3, 5, 6}, false))

	utils.AssertFalse(t, hasDouble([6]int{1, 2, 3, 6, 6, 6}, true))
	utils.AssertFalse(t, hasDouble([6]int{3, 3, 3, 1, 3, 6}, true))
	utils.AssertTrue(t, hasDouble([6]int{1, 1, 3, 4, 5, 6}, true))
	utils.AssertTrue(t, hasDouble([6]int{1, 1, 1, 3, 5, 5}, true))

	nextPassword := getNextValidPassword([6]int{1, 2, 3, 4, 5, 6}, false)
	expected := [6]int{1, 2, 3, 4, 6, 6}
	utils.AssertListEqual[[]int](t, nextPassword[:], expected[:])
}

func BenchmarkPart1(b *testing.B) {
	for i := 0; i < b.N; i++ {
		Part1("")
	}
}

func BenchmarkPart2(b *testing.B) {
	for i := 0; i < b.N; i++ {
		Part2("")
	}
}
