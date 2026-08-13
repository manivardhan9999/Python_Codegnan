Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Data type conversion
#bool
bool(7)
True
bool(2.0)
True
bool("Mani")
True
bool(5+2j)
True
bool(True)
True
bool(False)
False
#Int
int(6)
6
float(4.6)
4.6
int("Mani")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    int("Mani")
ValueError: invalid literal for int() with base 10: 'Mani'
int(5+3j)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    int(5+3j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
# In int string and complex could not converted

#float()
float(6)
6.0
float(6.0)
6.0
float("Mani")
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    float("Mani")
ValueError: could not convert string to float: 'Mani'
float(4+6j)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    float(4+6j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
#In float() string and complex cannot not convert

#str()
str(4)
'4'
str(4.6)
'4.6'
>>> str("Mani")
'Mani'
>>> str(4+6j)
'(4+6j)'
>>> str(True)
'True'
>>> #In str() All Data types can be converted
>>> 
>>> #complex()
>>> complex(2)
(2+0j)
>>> complex(2.0)
(2+0j)
>>> complex("Mani")
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    complex("Mani")
ValueError: complex() arg is a malformed string
>>> complex(4+6j)
(4+6j)
>>> complex(True)
(1+0j)
>>> #In complex str() cannot converted
>>> 
