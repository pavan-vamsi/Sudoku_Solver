def longest_unique_substring(s):
    n = len(s)
    char_index = {}
    max_length = 0
    start = 0  # Starting index of the sliding window

    for end in range(n):
        if s[end] in char_index:
            # Update start position of the window
            start = max(start, char_index[s[end]] + 1)
            print('if and for')
            print(char_index[s[end]] + 1)
        
        # Update the last index of the current character
        char_index[s[end]] = end
        print('to check')
        print(char_index[s[end]])
        # Update the maximum length of the substring
        max_length = max(max_length, end - start + 1)

    return max_length

# Example usage
s = "abcabcbb"
print(longest_unique_substring(s))  # Output: 3 (substring "abc")
