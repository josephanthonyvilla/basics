package main

import "fmt"

func search(datalist []int, key int) int {
	start := 0
	end := len(datalist) - 1
	for start <= end {
		mid := start + (end-start)/2
		if datalist[mid] == key {
			return mid
		}
		if datalist[mid] < key {
			start = mid + 1
		} else {
			end = mid - 1
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
	arr := []int{-5, 0, 1, 2, 9, 17, 42, 69}
	result(search(arr, 3))
	result(search(arr, 2))
}
