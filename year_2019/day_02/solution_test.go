package aoc_2019_02

import (
	"testing"

	utils "github.com/fitzgeraldkd/aoc/utils"
)

func TestPart1(t *testing.T) {
	utils.AssertEqual(t, Part1(""), 7210630)
}

func TestPart2(t *testing.T) {
	utils.AssertEqual(t, Part2(""), 3892)
}

func TestUtils(t *testing.T) {
	utils.AssertListEqual(
		t,
		runProgram([]int{1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50}),
		[]int{3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50},
	)

	utils.AssertListEqual(
		t,
		runProgram([]int{1, 0, 0, 0, 99}),
		[]int{2, 0, 0, 0, 99},
	)

	utils.AssertListEqual(
		t,
		runProgram([]int{2, 3, 0, 3, 99}),
		[]int{2, 3, 0, 6, 99},
	)

	utils.AssertListEqual(
		t,
		runProgram([]int{2, 4, 4, 5, 99, 0}),
		[]int{2, 4, 4, 5, 99, 9801},
	)

	utils.AssertListEqual(
		t,
		runProgram([]int{1, 1, 1, 4, 99, 5, 6, 0, 99}),
		[]int{30, 1, 1, 4, 2, 5, 6, 0, 99},
	)
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
