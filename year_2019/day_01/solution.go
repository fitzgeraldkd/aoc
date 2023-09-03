package aoc_2019_01

import (
	utils "github.com/fitzgeraldkd/aoc/utils"
)

func getInputs(filepath string) []int {
	return utils.GetIntLines(filepath)
}

func getFuel(mass int) int {
	return (mass / 3) - 2
}

func Part1(filepath string) int {
	inputs := getInputs(filepath)
	totalFuel := 0
	for _, mass := range inputs {
		totalFuel += getFuel(mass)
	}
	return totalFuel
}

func Part2(filepath string) int {
	inputs := getInputs(filepath)
	totalFuel := 0
	for _, mass := range inputs {
		thisFuel := getFuel(mass)
		for thisFuel > 0 {
			totalFuel += thisFuel
			thisFuel = getFuel(thisFuel)
		}
	}
	return totalFuel
}
