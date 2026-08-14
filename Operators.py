Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Arithmetic
a = 4
b = 6
print(a+b)
10
print(a-b)
-2
print(a*b)
24
print(a//b)
0
print(a%b)
4
print(a**b)
4096

#Assingment
a = 2
b = 4
a += b
a
6
b
4
b -= 2
b
2
b *= 1
b
2
b /= 2
b
1.0
b //= 2
b
0.0
b %= 5
b
0.0
b = 10
b **= 2
b
100

#Comparision
a = 4
b = 6
a < b
True
a > b
False
b < a
False
b > a
True
a != b
True
a == b
False
a >= b
False
a <= b
True

#Logical
a = 2
b = 3
a < b and b > a
True
a > b and b > a
False
a != b and a==b
False
not True
False
not False
True
a >= b or b <= a
False
a < b or b < a
True

#Identify
a = 4
type(a) is int
True
type(a) is float
False
a = 2.2
type(a) is not int
True

#membership
a = 3,4,5,6
6 in a
True
2 not in a
True

#Bitwise
a = 2
b = 4
a & b
0
bin(2)
'0b10'
bin(a)
'0b10'
a | b
6
a | a
2
>>> a = 8
>>> ~a
-9
>>> a = 8
>>> b = 9
>>> a^b
1
>>> a=3
>>> b=7
>>> a^b
4
>>> a >>
SyntaxError: invalid syntax
>>> SyntaxError: invalid syntax
SyntaxError: invalid syntax
>>> a = 3
>>> a >> 3
0
>>> a << 3
24
>>> a = 2
>>> b = 4
>>> a^b
6
