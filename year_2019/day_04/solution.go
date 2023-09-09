package aoc_2019_04

import (
	"strconv"
	"strings"

	utils "github.com/fitzgeraldkd/aoc/utils"
)

func getInputs(filepath string) [][6]int {
	stringRange := strings.Split(utils.GetLines(filepath)[0], "-")
	var intRange [][6]int
	for _, stringValue := range stringRange {
		var password [6]int
		for i := 0; i < len(stringValue); i++ {
			password[i], _ = strconv.Atoi(stringValue[i : i+1])
		}
		intRange = append(intRange, password)
	}
	return intRange
}

func hasDouble(password [6]int, strict bool) bool {
	for i, value := range password {
		if i > 0 && value == password[i-1] {
			if strict && ((i > 1 && password[i-2] == value) || (i < len(password)-1 && password[i+1] == value)) {
				continue
			}
			return true
		}
	}
	return false
}

func concatPassword(passwordArr [6]int) int {
	password := 0
	for i := 0; i < len(passwordArr); i++ {
		password += passwordArr[len(passwordArr)-i-1] * utils.PowInt(10, i)
	}
	return password
}

func getNextValidPassword(password [6]int, strict bool) [6]int {
	for i := 1; i < len(password); i++ {
		if password[i] < password[i-1] {
			for j := i; j < len(password); j++ {
				password[j] = password[i-1]
			}
			if hasDouble(password, strict) {
				return password
			} else {
				return getNextValidPassword(password, strict)
			}
		}
	}

	for i := len(password) - 1; i >= 0; i-- {
		for password[i] < 9 {
			password[i]++
			for j := i + 1; j < len(password); j++ {
				password[j] = password[i]
			}
			if hasDouble(password, strict) {
				return password
			} else {
				return getNextValidPassword(password, strict)
			}
		}
	}
	return [6]int{-1, -1, -1, -1, -1, -1}
}

func Part1(filepath string) int {
	inputs := getInputs(filepath)
	password := getNextValidPassword(inputs[0], false)
	maxPassword := concatPassword(inputs[1])
	var validPasswords []int
	for concatPassword(password) < maxPassword {
		validPasswords = append(validPasswords, concatPassword(password))
		password = getNextValidPassword(password, false)
		if password[0] == -1 {
			break
		}
	}
	return len(validPasswords)
}

func Part2(filepath string) int {
	inputs := getInputs(filepath)
	password := getNextValidPassword(inputs[0], true)
	maxPassword := concatPassword(inputs[1])
	var validPasswords []int
	for concatPassword(password) < maxPassword {
		validPasswords = append(validPasswords, concatPassword(password))
		password = getNextValidPassword(password, true)
		if password[0] == -1 {
			break
		}
	}
	return len(validPasswords)
}
