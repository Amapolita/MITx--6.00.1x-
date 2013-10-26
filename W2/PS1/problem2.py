'''

COUNTING BOBS  (15.0/15.0 points)
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, 
if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2

x = empty string 
occ = number of occurrences.


'''

x = ''
occ = 0

for i in s:
    x += i
    if 'bob' in x:
        occ += 1
        x = x [-1]
        
print occ
