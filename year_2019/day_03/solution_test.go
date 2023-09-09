package aoc_2019_03

import (
	"testing"

	utils "github.com/fitzgeraldkd/aoc/utils"
)

func TestPart1(t *testing.T) {
	utils.AssertEqual(t, Part1(""), 225)
	utils.AssertEqual(t, Part1("sampleA.txt"), 6)
	utils.AssertEqual(t, Part1("sampleB.txt"), 159)
	utils.AssertEqual(t, Part1("sampleC.txt"), 135)
}

func TestPart2(t *testing.T) {
	utils.AssertEqual(t, Part2(""), 35194)
	utils.AssertEqual(t, Part2("sampleA.txt"), 30)
	utils.AssertEqual(t, Part2("sampleB.txt"), 610)
	utils.AssertEqual(t, Part2("sampleC.txt"), 410)
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
