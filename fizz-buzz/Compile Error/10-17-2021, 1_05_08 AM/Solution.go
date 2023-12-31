// https://leetcode.com/problems/fizz-buzz

import "strconv"

func fizzBuzz(n int) []string {
    arr := make([]string, n)
    for i := 0; i < n; i++ {
        if i % 5 == 0 && i % 3 == 0 {
            arr[i] = "FizzBuzz"
        }
        else if i % 3 == 0 {
            arr[i] = "Fizz"
        }
        else if i % 5 == 0 {
            arr[i] = "Buzz"
        }
        else {
            arr[i] = strconv.Itoa(i)
        }
    }
    return arr
}