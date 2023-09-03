package aoc_2019_02

import (
	utils "github.com/fitzgeraldkd/aoc/utils"
)

func getInputs(filepath string) []int {
	return utils.GetIntCSV(filepath)
}

func runAdd(intcode []int, args []int) []int {
	intcode[args[2]] = intcode[args[0]] + intcode[args[1]]
	return intcode
}

func runMult(intcode []int, args []int) []int {
	intcode[args[2]] = intcode[args[0]] * intcode[args[1]]
	return intcode
}

func runProgram(intcode []int) []int {
	index := 0
	for index < len(intcode) {
		opcode := intcode[index]
		if opcode == 1 {
			runAdd(intcode, intcode[index+1:index+4])
		} else if opcode == 2 {
			runMult(intcode, intcode[index+1:index+4])
		} else if opcode == 99 {
			return intcode
		} else {
			return []int{}
		}
		index += 4
	}
	return intcode
}

func Part1(filepath string) int {
	intcode := getInputs(filepath)
	intcode[1] = 12
	intcode[2] = 2
	intcode = runProgram(intcode)

	return intcode[0]
}

func Part2(filepath string) int {
	origIntcode := getInputs(filepath)
	const target = 19690720
	var noun int
	var verb int
	var output int
	for noun = 0; noun <= 99; noun++ {
		for verb = 0; verb <= 99; verb++ {
			intcode := make([]int, len(origIntcode))
			copy(intcode, origIntcode)
			intcode[1] = noun
			intcode[2] = verb
			intcode = runProgram(intcode)
			if len(intcode) == 0 {
				continue
			}
			output = intcode[0]
			if output == target {
				break
			}
		}
		if output == target {
			break
		}
	}
	return noun*100 + verb
}
