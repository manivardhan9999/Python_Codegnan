Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Indexing
a = "Vijayawada"
a[0]
'V'
a[0]+a[1]+a[2]+a[3]+a[4]
'Vijay'
b = "Iam in class"
b[7]+b[8]+b[9]+b[10]+b[11]
'class'
b[3]+b[6]
'  '
c = "I am Learning Python"
c[5]+c[6]+c[7]+c[8]+c[9]
'Learn'
c[14]+c[15]+c[16]+c[17]+c[18]+c[19]
'Python'
d = "Codegnan IT Solutions"
d[0]+d[1]+d[2]+d[3]
'Code'
d[12]+d[13]+d[14]+d[15]+d[16]+d[17]+d[18]+d[19]+d[20]
'Solutions'
e = "Time is Very Precious"
e[-1]+a[-2]+e[-3]+e[-4]+e[-5]+e[-6]+e[-7]+e[-8]
'sdoicerP'
e[-10]+e[-11]+e[-12]+e[-13]
'yreV'
e[-15]+e[-16]
'si'
e[-16]+e[-15]
'is'
e[-13]+e[-12]+e[-11]+e[-10]
'Very'
a ="Hello Hi How are you"
# you, hello, how
a[-3]+a[-2]+a[-1]
'you'
a[-20]+a[-19]+a[-18]+a[-17]+a[-16]
'Hello'
a[-11]+a[-10]+a[-9]
'How'
#Slicing--------------------------------------------------------------------------------------
a = "Codegnan"
a[0:4]
'Code'
a[4:8]
'gnan'
b = "work untill you succeed"
b[0:5]
'work '
b[7:13]
'till y'
b[5:12]
'untill '
b[13:16]
'ou '
b[12:16]
'you '
b[16:23]
'succeed'
c ="simple is better than complex"
c[0:6]
'simple'
c[7:9]
'is'
d = "Vizag is city of destiny"
d[-24]+d[-23]+d[-22]+d[-21]+d[-20]
'Vizag'
d[-24:-19]
'Vizag'
d[-18:-16]
'is'
d[-15:-11]
'city'
d[-10:-8]
'of'
d[-7: ]
'destiny'
#Striding-----------------------------------------------------------------------------------
a = "Machine learning"
a[::5]
'Mnag'
a[::7]
'M n'
a[::2]
'Mcielann'
a[::6]
'Men'
a[7: ]
' learning'
a[:9]
'Machine l'
a[ :9]
'Machine l'
a[6: ]
'e learning'
a[2:8]
'chine '
>>> a[5:12]
'ne lear'
>>> n = "Cloud Computing"
>>> n[2:13:3]
'o mt'
>>> a[5:14:4]
'nei'
>>> a[3:12:6]
'he'
>>> n[5:14:4]
' pn'
>>> n[3:12:6]
'up'
>>> m = "Python Course"
>>> a[-1:-9:-2]
'gire'
>>> m[-1:-9:-2]
'ero '
>>> m[::-2]
'ero otP'
>>> m[-4:-13:-5]
'uo'
>>> m[-2:-12:-3]
'sont'
