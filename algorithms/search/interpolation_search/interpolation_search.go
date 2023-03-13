package main

import "fmt"

func search(arr []int, low int, high int, key int) int {
	if arr[high] == arr[low] {
		return high
	}
	if low <= high && key >= arr[low] && key <= arr[high] {

		idx := low + (((high - low) / (arr[high] - arr[low])) * (key - arr[low]))

		if arr[idx] == key {
			return idx
		}
		if arr[idx] < key {
			return search(arr, idx+1, high, key)
		}
		if arr[idx] > key {
			return search(arr, low, idx-1, key)
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
	arr := []int{11, 12, 14, 17, 19, 20, 21, 22, 25, 34, 36, 42, 47}
	n := len(arr) - 1
	result(search(arr, 0, n, 23))
	result(search(arr, 0, n, 11))
	result(search(arr, 0, n, 22))
	result(search(arr, 0, n, 47))
}
