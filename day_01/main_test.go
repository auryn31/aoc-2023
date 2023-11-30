package aoc


import (
  "testing"
  "os"
)

func TestAdd(t *testing.T){

	dat, err := os.ReadFile("input.txt")
  Check(err)

  got := DayOne(string(dat))
  want := "Hello"


    if got != want {
        t.Errorf("got %q, wanted %q", got, want)
    }
}
