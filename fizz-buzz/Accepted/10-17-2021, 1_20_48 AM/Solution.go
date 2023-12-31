// https://leetcode.com/problems/fizz-buzz

import "strconv"

func fizzBuzz(n int) []string {
    arr := make([]string, n)
    for i := 1; i <= n; i++ {
        if i % 15 == 0 {
            arr[i-1] = "FizzBuzz"
        } else if i % 3 == 0 {
            arr[i-1] = "Fizz"
        } else if i % 5 == 0 {
            arr[i-1] = "Buzz"
        } else {
            arr[i-1] = strconv.Itoa(i)
        }
    }
    return arr
}