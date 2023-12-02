package aoc

import (
  "strings"
  "strconv"
  "errors"
)

func Check(e error) {
	if e != nil {
		panic(e)
	}
}


func DayOne(input string) (int) {
  lines := strings.Split(input, "\n")

  sum := 0
  for _, line := range lines {
    if len(line) == 0 {
      continue
    }
    val, err := isGamePossible(line)
    if err == nil {
      sum += val
    }
  }
  return sum
}
func DayTwo(input string) (int) {
  lines := strings.Split(input, "\n")

  sum := 0
  for _, line := range lines {
    if len(line) == 0 {
      continue
    }
    val := powerOfGame(line)
    sum += val
  }
  return sum
}

func numFromColor()(map[string]int) {
  m := make(map[string]int)
  m["red"] = 12
  m["blue"] = 14
  m["green"] = 13
  return m
}

func powerOfGame(line string) (int) {

  sum := 0
  setLine := strings.Split(line, ":")[1]
  m := make(map[string]int)

  elements := strings.Split(setLine, ";")
  print("elements: ", elements, "\n")
  for _, set := range elements {
  print("set: ", set, "\n")
    for _, entry := range strings.Split(set, ",") {
      numStr := strings.Split(strings.TrimSpace(entry), " ")[0]
      color := strings.Split(strings.TrimSpace(entry), " ")[1]
      num, err := strconv.Atoi(numStr)
      if err != nil {
        panic(1)
      }
      print("num: ", num, " color: ", color, "\n")
      current, ok := m[color]
      if ok {
        if num > current {
          m[color] = num
        }
      } else {
        m[color] = num
      }
    }
  }

sum = 1
  for _, val := range m {
  sum *= val

  }

  return sum
}
func isGamePossible(line string) (int, error) {
  gameId, err := strconv.Atoi(strings.Split(strings.Split(line, ":")[0], " ")[1])
  if err != nil {
    print("Fail on gameId\n")
    return 0, err
  }

  setLine := strings.Split(line, ":")[1]

  elements := strings.Split(setLine, ";")
  print("elements: ", elements, "\n")
  for _, set := range elements {
  print("set: ", set, "\n")
    for _, entry := range strings.Split(set, ",") {
      numStr := strings.Split(strings.TrimSpace(entry), " ")[0]
      color := strings.Split(strings.TrimSpace(entry), " ")[1]
      num, err := strconv.Atoi(numStr)
      if err != nil {
        print(" Fail on num Pars\n")
        return 0, err
      }
      print("num: ", num, " color: ", color, "\n")
      if num > numFromColor()[color] {
        err := errors.New("Value to big\n")
        print("Value to big\n")
        return 0, err
      }
    }
  }

  return gameId, nil
}
