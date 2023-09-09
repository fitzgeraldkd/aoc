package utils

import (
	"strconv"
	"strings"
)

const UP = 'u'
const LEFT = 'l'
const RIGHT = 'r'
const DOWN = 'd'

var VECTORS = map[rune][2]int{
	DOWN:  {0, -1},
	LEFT:  {-1, 0},
	RIGHT: {1, 0},
	UP:    {0, 1},
}

type GridMap[T any] map[string]T

func CoordToString(coord []int) string {
	stringSlice := make([]string, len(coord))
	for i, value := range coord {
		stringSlice[i] = strconv.Itoa(value)
	}
	return strings.Join(stringSlice, ",")
}

func CoordToIntSlice(coord string) []int {
	stringSlice := strings.Split(coord, ",")
	intSlice := make([]int, len(stringSlice))
	for i, value := range stringSlice {
		intSlice[i], _ = strconv.Atoi(value)
	}
	return intSlice
}

func GetManhattanDistance(coord1 []int, coord2 []int) int {
	if len(coord1) == len(coord2) {
		distance := 0
		for i, v := range coord1 {
			var vector int
			if v > coord2[i] {
				vector = v - coord2[i]
			} else {
				vector = coord2[i] - v
			}
			distance += vector
		}
		return distance
	} else {
		return -1
	}
}
