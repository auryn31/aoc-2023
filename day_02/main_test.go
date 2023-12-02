package aoc


import (
  "testing"
  "os"
)

func TestDayOne(t *testing.T){
	dat, err := os.ReadFile("input.txt")
  Check(err)

  got := DayOne(string(dat))
  want := 3035
    if got != want {
        t.Errorf("got %d, wanted %d", got, want)
    }
}

func TestDayTwo(t *testing.T){
	dat, err := os.ReadFile("input.txt")
  Check(err)

  got := DayTwo(string(dat))
  want := 66027
    if got != want {
        t.Errorf("got %d, wanted %d", got, want)
    }
}
