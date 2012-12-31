package main

import "fmt"

func main() {
	var ss string
	m := make(map[rune]int)
	fmt.Scanf("%s", &ss)
	for _, c := range ss {
		m[c] += 1
	}
	fmt.Println(m['A'], m['C'], m['T'], m['G'])
}
