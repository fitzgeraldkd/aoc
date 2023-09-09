package aoc_20XX_XX

import (
	"testing"

	utils "github.com/fitzgeraldkd/aoc/utils"
)

func TestPart1(t *testing.T) {
	utils.AssertEqual(t, Part1(""), -1)
}

func TestPart2(t *testing.T) {
	utils.AssertEqual(t, Part2(""), -1)
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
