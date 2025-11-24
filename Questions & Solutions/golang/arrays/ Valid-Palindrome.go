package arrays

func isPalindrome(s string) bool {
   
    left, right := 0, len(s)-1

    for left < right {
        // Move left forward if not alphanumeric
        for left < right && !isAlphaNum(s[left]) {
            left++
        }

        // Move right backward if not alphanumeric
        for left < right && !isAlphaNum(s[right]) {
            right--
        }

        // Compare lowercase versions
        if toLower(s[left]) != toLower(s[right]) {
            return false
        }

        left++
        right--
    }

    return true
}

// helper: check alphanumeric
func isAlphaNum(c byte) bool {
    return (c >= 'a' && c <= 'z') ||
           (c >= 'A' && c <= 'Z') ||
           (c >= '0' && c <= '9')
}

// helper: lowercase conversion
func toLower(c byte) byte {
    if c >= 'A' && c <= 'Z' {
        return c + 32
    }
    return c
}