package aoc_2019_03

import (
	"fmt"
	"strconv"
	"strings"
	"unicode"

	utils "github.com/fitzgeraldkd/aoc/utils"
)

type vector struct {
	direction rune
	distance  int
}

type path []vector

func getInputs(filepath string) []path {
	lines := utils.GetLines(filepath)
	var paths []path
	for _, wire := range lines {
		vectors := strings.Split(wire, ",")
		var path path
		for _, vectorString := range vectors {
			var direction rune
			for _, char := range vectorString {
				direction = unicode.ToLower(char)
				break
			}
			distance, _ := strconv.Atoi(vectorString[1:])
			var vector = vector{
				direction: direction,
				distance:  distance,
			}
			path = append(path, vector)
		}
		paths = append(paths, path)
	}
	return paths
}

func getWireMap(path path) utils.GridMap[int] {
	grid := utils.GridMap[int]{}
	coord := [2]int{0, 0}
	length := 0
	for _, vector := range path {
		for i := 0; i < vector.distance; i++ {
			delta := utils.VECTORS[vector.direction]
			length++
			coord[0] += delta[0]
			coord[1] += delta[1]
			coordString := fmt.Sprintf("%d,%d", coord[0], coord[1])
			grid[coordString] = length
		}
	}
	return grid
}

func Part1(filepath string) int {
	paths := getInputs(filepath)
	grid1 := getWireMap(paths[0])
	grid2 := getWireMap(paths[1])
	minDistance := -1
	for coord := range grid2 {
		if _, exists := grid1[coord]; exists {
			coordInt := utils.CoordToIntSlice(coord)
			distance := utils.GetManhattanDistance(coordInt, []int{0, 0})
			if (minDistance == -1) || (distance < minDistance) {
				minDistance = distance
			}
		}
	}
	return minDistance
}

func Part2(filepath string) int {
	paths := getInputs(filepath)
	grid1 := getWireMap(paths[0])
	grid2 := getWireMap(paths[1])
	minDistance := -1
	for coord, length1 := range grid2 {
		if length2, exists := grid1[coord]; exists {
			distance := length1 + length2
			if (minDistance == -1) || (distance < minDistance) {
				minDistance = distance
			}
		}
	}
	return minDistance
}
