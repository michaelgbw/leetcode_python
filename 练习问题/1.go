package main

//给定一个字符串，要求把字符串前面的若干个字符移动到字符串的尾部，
//如把字符串“abcdef”前 面的 2 个字符'a'和'b'移动到字符串的尾部，使得原字符串变成字符串“cdefab”。
//请写一个函数完 成此功能，要求对长度为 n 的字符串操作的时间复杂度为 O(n)，空间复杂度为 O(1)。

import (
	"fmt"
	"strings"
)

func reverse(s *[]string, from int, to int) {
	for to > from {
		tmp := (*s)[to]
		(*s)[to] = (*s)[from]
		(*s)[from] = tmp
		to -= 1
		from += 1
	}
}

func main() {
	s := "abcdefg"
	slist := strings.Split(s, "")
	m := 3
	n := len(slist)
	reverse(&slist, 0, m-1)

	reverse(&slist, m, n-1)
	reverse(&slist, 0, n-1)
	fmt.Println(slist)
}
