package main

import "fmt"

func search(datalist []int, key int) int {
	for i := 0; i < len(datalist); i++ {
		if datalist[i] == key {
			return i
		}
	}
	return -1
}

func result(idx int) {
	if idx == -1 {
		fmt.Println("Element not found")
	} else {
		fmt.Println("Element found at index", idx)
	}
}

func main() {
	arr := []int{0, 42, 69, 17, -5, 2, 9, 1}
	result(search(arr, 3))
	result(search(arr, 2))
}
