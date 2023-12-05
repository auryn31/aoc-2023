package aoc

import (
	"strconv"
	"strings"
)

func Check(e error) {
	if e != nil {
		panic(e)
	}
}

func DayOne(input string) int {
	lines := strings.Split(input, "\n")

	grid := []
	for _, line := range lines {
		if len(line) == 0 {
			continue
		}
		grid = append(grid, strings.Split(line, ""))
	}

	sum := 0
	for i, line := range grid {
		currentNum := ""
		for j, char := range line {
			_, err := strconv.Atoi(char)
			if err == nil {
				currentNum += char
			}
			if err != nil && len(currentNum) > 0 {
				print("currentNum: ", currentNum, "\n")
				num, _ := strconv.Atoi(currentNum)
				if numIsValid(grid, len(lines), len(line), i-len(line)-1, j-1, num) {
					sum += num
				}
				currentNum = ""

			}
		}

	}
	return sum
}

func isSymbol(char string) bool {
	return char != "."
}

func numIsValid(grid [][]string, rowLength int, colLength int, posRow int, posCol int, number int) bool {
	numLength := len(strconv.Itoa(number)) - 1
	// first position
	if posRow == 0 && posCol-numLength == 0 {
		print("posRow: ", posRow, " posCol: ", posCol, "\n")
		print("length number ", numLength, "\n")
		if isSymbol(grid[posRow+1][posCol]) || isSymbol(grid[posRow][posCol+1]) || isSymbol(grid[posRow+1][posCol+1]) {
			return true
		} else {
			return false
		}

	}

	// first element in all rows except last
	if posRow < rowLength-1 && posCol == 0 {
		if isSymbol(grid[posRow-numLength][posCol]) || isSymbol(grid[posRow+1][posCol]) || isSymbol(grid[posRow][posCol+1]) || isSymbol(grid[posRow+1][posCol+1]) {
			return true
		} else {
			return false
		}

	}

	// first element in last rows
	if posRow < rowLength && posCol == 0 {
		if isSymbol(grid[posRow-numLength][posCol]) || isSymbol(grid[posRow][posCol+1]) || isSymbol(grid[posRow+1][posCol+1]) {
			return true
		} else {
			return false
		}
	}

	// all elements in first row
	if posRow == 0 && posCol < colLength-1 {
		if isSymbol(grid[posRow+1][posCol]) || isSymbol(grid[posRow][posCol+1]) || isSymbol(grid[posRow+1][posCol+1]) || isSymbol(grid[posRow][posCol-numLength]) || isSymbol(grid[posRow+1][posCol-numLength]) {
			return true
		} else {
			return false
		}
	}

	// all elements in first row
	if posRow == 0 && posCol == colLength-1 {
		if isSymbol(grid[posRow-numLength][posCol]) || isSymbol(grid[posRow+1][posCol-numLength]) || isSymbol(grid[posRow+1][posCol]) {
			return true
		} else {
			return false
		}

	}

	return false

}
