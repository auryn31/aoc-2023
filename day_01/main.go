package aoc

import (
	"fmt"
	"os"
  "strings"
  "strconv"
  "errors"
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

func DayOne(input string) (int) {
  lines := strings.Split(input, "\n")
  sum := 0
  for _, line := range lines {
    if len(line) == 0 {
      continue
    }
    chars := strings.Split(line, "")
    numbers := make([]int, 0)
    for _, char := range chars {
      num, err := strconv.Atoi(char)
      if err == nil {
        numbers = append(numbers, num)
      }
  }
    first := numbers[0]
    last := numbers[len(numbers)-1]
    sum += 10*first + last
  }

  return sum

}

func getNumFromString(subString string) (int, error) {
  if strings.HasPrefix(subString,"one"){

    return 1, nil
  }
    if strings.HasPrefix(subString,"two"){

    return 2, nil
  }

  if strings.HasPrefix(subString,"three"){

    return 3, nil
  }
  if strings.HasPrefix(subString,"four"){

    return 4, nil
  }
  if strings.HasPrefix(subString,"five"){

    return 5, nil
  }
  if strings.HasPrefix(subString,"six"){

    return 6, nil
  }
  if strings.HasPrefix(subString,"seven"){

    return 7, nil
  }
  if strings.HasPrefix(subString,"eight"){

    return 8,nil
  }

  if strings.HasPrefix(subString,"nine"){

    return 9,nil
  }

  return 0, errors.New("No number found")

}

func DayTwo(input string) (int) {
  lines := strings.Split(input, "\n")
  sum := 0
  for _, line := range lines {
    if len(line) == 0 {
      continue
    }
    chars := strings.Split(line, "")
    numbers := make([]int, 0)
    for i, char := range chars {
      num, err := strconv.Atoi(char)
      if err == nil {
        numbers = append(numbers, num)
      }
      substring := line[i:]
      num, err = getNumFromString(substring)
      if err == nil {
      numbers = append(numbers, num)
            }

      
  }
    first := numbers[0]
    last := numbers[len(numbers)-1]
    sum += 10*first + last
  }

  return sum

}
