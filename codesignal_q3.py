
""" 
# CodeSignal Example Q3
# You are implementing your own programming language and you've decided to add support for merging strings. A typical merge function would take two strings s1 and s2, and return the lexicographically smallest result that can be obtained by placing the symbols of s2 between the symbols of s1 in such a way that maintains the relative order of the characters in each string.

For example, if s1 = "super" and s2 = "tower", the result should be merge(s1, s2) = "stouperwer".



You'd like to make your language more unique, so for your merge function, instead of comparing the characters in the usual lexicographical order, you'll compare them based on how many times they occur in their respective initial strings (fewer occurrences means the character is considered smaller). If the number of occurrences are equal, then the characters should be compared in the usual lexicographical way. If both number of occurences and characters are equal, you should take the characters from the first string to the result. Note that occurrences in the initial strings are compared - they do not change over the merge process.

Given two strings s1 and s2, return the result of the special merge function you are implementing.

Example

For s1 = "dce" and s2 = "cccbd", the output should be
solution(s1, s2) = "dcecccbd".
All symbols from s1 goes first, because all of them have only 1 occurrence in s1 and c has 3 occurrences in s2.



For s1 = "super" and s2 = "tower", the output should be
solution(s1, s2) = "stouperwer".
Because in both strings all symbols occur only 1 time, strings are merged as usual. You can find explanation for this example on the image in the description.

Input/Output

[execution time limit] 4 seconds (py3)

[input] string s1

A string consisting only of lowercase English letters.

Guaranteed constraints:
1 ≤ s1.length ≤ 104.

[input] string s2

A string consisting only of lowercase English letters.

Guaranteed constraints:
1 ≤ s2.length ≤ 104.

[output] string

The string that results by merging s1 and s2 using your special merge function.
 """

        
    
# CodeSignals

def solution(s1, s2):
    
    # get occurences of characters in a hashmap for each string
    s1_freq = {}
    for char in s1:
        s1_freq[char] = s1_freq.get(char, 0) + 1
        
    s2_freq = {}
    for char in s2:
        s2_freq[char] = s2_freq.get(char, 0) + 1

    # use two-pointers approach
    s1_pos = 0
    s2_pos = 0
    
    # merge sub-function, smallest wins
    # params: char1, char2
    # returns: character and word
    def merge(char1, char2):
        # if char1 occurs more frequently, return 
        if s1_freq[char1] < s2_freq[char2]:
            # char1 wins
            return char1, "s1"
        elif s1_freq[char1] > s2_freq[char2]:
            # char2 wins
            return char2, "s2"
        else:
            if char1 < char2:
                # char1 wins
                return char1, "s1"
            elif char2 < char1:
                # char2 wins
                return char2, "s2"
            else:
                # result is char1 - char1 wins
                return char1, "s1"
            
    # main comparison 
    # while they both have characters
    
    # define result string
    res_str = ""
    
    while s1_pos < len(s1) and s2_pos < len(s2):
        char1 = s1[s1_pos]
        char2 = s2[s2_pos]
        smaller_res = merge(char1, char2)
        res_str += smaller_res[0]
        # only move position of winner
        print(smaller_res[1])
        if smaller_res[1] == "s1":    
            s1_pos += 1 
        else:    
            s2_pos += 1
        
    # if s1 is the one with chars left, append it to res_str
    if s1_pos < len(s1):
        res_str += s1[s1_pos:]
        
    # if s2 is the one with chars left, append it to res_str
    if s2_pos < len(s2):
        res_str += s2[s2_pos:]
    
    print(res_str)
    
    return res_str
     