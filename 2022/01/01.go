package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func check(err error) {
	if err != nil {
		fmt.Fprintf(os.Stderr, "[E] %v\n", err)
		os.Exit(1)
	}
}

func main() {
	infile, err := os.Open("./input.txt")
	check(err)

	calorieSums := make([]int, 0)

	curSum := 0
	reader := bufio.NewReader(infile)
	for line, err := reader.ReadString('\n'); err == nil; line, err = reader.ReadString('\n') {
		line = strings.TrimSpace(line)
		if line == "" {
			calorieSums = append(calorieSums, curSum)
			curSum = 0
		} else {
			lineInt, cerr := strconv.Atoi(line)
			check(cerr)
			curSum += lineInt
		}
	}
	if curSum > 0 {
		// no empty line at end of file
		// append last elf's sum
		calorieSums = append(calorieSums, curSum)
	}

	sort.Ints(calorieSums)

	nElfs := len(calorieSums)
	fmt.Printf("Max calories on a single elf: %d\n", calorieSums[nElfs-1])
	fmt.Printf("Top 3 stashes: %+v\n", calorieSums[nElfs-3:])
	fmt.Printf("Sum of top 3 stashes: %d\n", sum(calorieSums[nElfs-3:]))
}

func sum(s []int) int {
	sum := 0
	for _, v := range s {
		sum += v
	}
	return sum
}
