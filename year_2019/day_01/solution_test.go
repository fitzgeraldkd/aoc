package aoc_2019_01

import (
	"testing"

	utils "github.com/fitzgeraldkd/aoc/utils"
)

func TestPart1(t *testing.T) {
	utils.AssertEqual(t, Part1("sample1.txt"), 34241)
	utils.AssertEqual(t, Part1(""), 3173518)
}

func TestPart2(t *testing.T) {
	utils.AssertEqual(t, Part2("sample2a.txt"), 2)
	utils.AssertEqual(t, Part2("sample2b.txt"), 966)
	utils.AssertEqual(t, Part2("sample2c.txt"), 50346)
	utils.AssertEqual(t, Part2(""), 4757427)
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
