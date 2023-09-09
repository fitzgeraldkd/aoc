package utils

import (
	"bufio"
	"os"
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
	return StringSliceToInt(lines)
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
	return StringSliceToInt(stringValues)
}
