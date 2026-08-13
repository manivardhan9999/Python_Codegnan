Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Data types
a = 10
type(a)
<class 'int'>
b = 4.6
type(b)
<class 'float'>
c = 'code'
type(c)
<class 'str'>
d="code"
type(d)
<class 'str'>
>>> e = 5+6j
>>> type(e)
<class 'complex'>
>>> r = 5+7i
SyntaxError: invalid decimal literal
>>> y = j
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    y = j
NameError: name 'j' is not defined
>>> e = True
>>> type(e)
<class 'bool'>
>>> h = 9j
>>> type(h)
<class 'complex'>
>>> c = "true"
>>> type(c)
<class 'str'>
>>> c = true
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    c = true
NameError: name 'true' is not defined. Did you mean: 'True'?
