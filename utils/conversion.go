package utils

import (
	"strconv"
)

func StringSliceToInt(stringSlice []string) []int {
	intSlice := make([]int, len(stringSlice))
	for i, stringValue := range stringSlice {
		intValue, _ := strconv.Atoi(stringValue)
		intSlice[i] = intValue
	}
	return intSlice
}
