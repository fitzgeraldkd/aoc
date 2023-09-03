package utils

import (
	"bufio"
	"os"
	"strconv"
	"strings"
)

func GetFile(filepath string) *os.File {
	if filepath == "" {
		filepath = "inputs.txt"
	}
	file, _ := os.Open(filepath)
	return file
}

func GetLines(filepath string) []string {
	file := GetFile(filepath)
	scanner := bufio.NewScanner(file)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	return lines
}

func GetIntLines(filepath string) []int {
	lines := GetLines(filepath)
	intLines := make([]int, len(lines))
	for i, line := range lines {
		value, _ := strconv.Atoi(line)
		intLines[i] = value
	}
	return intLines
}

func GetCSV(filepath string) []string {
	file := GetFile(filepath)
	scanner := bufio.NewScanner(file)
	scanner.Scan()
	values := strings.Split(scanner.Text(), ",")
	return values
}

func GetIntCSV(filepath string) []int {
	stringValues := GetCSV(filepath)
	intValues := make([]int, len(stringValues))
	for i, value := range stringValues {
		intValue, _ := strconv.Atoi(value)
		intValues[i] = intValue
	}
	return intValues
}
