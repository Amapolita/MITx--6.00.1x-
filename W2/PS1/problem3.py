'''
ALPHABETICAL SUBSTRINGS  (15.0/15.0 points)
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh


In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

For problems such as these, do not include raw_input statements or define the variable s in any way. 
Our automating testing will provide a value of s for you - 
so the code you submit in the following box should assume s is already defined. 
If you are confused by this instruction, please review L4 Problems 10 and 11 before you begin this problem set.

Note: This problem is fairly challenging. We encourage you to work smart. 
If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course. 
If you have time, come back to this problem after you've had a break and cleared your head.

'''
s = 'azcbobobegghakl'
first,last = 0,0
long_string = []
for letter in range(len(s)+1):
    if  letter !=(len(s)) and ord(s[letter])>= ord(s[letter-1]):
            last = letter
    else:
            long_string.append(s[first:last+1])
            first,last = letter, letter
print "Longest substring in alphabetical order is: "  + max(long_string, key=len)

