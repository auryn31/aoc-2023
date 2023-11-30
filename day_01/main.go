package aoc

import (
	"fmt"
	"os"
)

func Check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	dat, err := os.ReadFile("input.txt")
  Check(err)

  result := DayOne(string(dat))

	fmt.Println(result)

}

func DayOne(input string) (string) {
  return "Hello"
}
