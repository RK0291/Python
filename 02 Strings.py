>>> "Welcome"
'Welcome'
>>> 'Welcome'
'Welcome'
>>> 'Welcome to \n Code Shala'
'Welcome to \n Code Shala'
>>> print('Welcome to \n Code Shala')
Welcome to 
 Code Shala
>>> print('Welcome to \nCode Shala')
Welcome to 
Code Shala
>>> print(r'Welcome to \n Code Shala')
Welcome to \n Code Shala
>>> print(r'Welcome to Code Shala')
Welcome to Code Shala
>>> print('C:\Users\name')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> print(r'C:\Users\name')
C:\Users\name

Strings can be concatenated (glued together) with the + operator, and repeated with *:
>>> 2 * 'un' + 'ion'
'ununion'

>>> 'code' 'shala'
'codeshala'

>>> fname = 'Code'
>>> fname 'shala'
SyntaxError: invalid syntax
>>> 'You cant concatenate a variable with a string'
'You cant concatenate a variable with a string'
'Please use a + operator'
>>> fname + 'shala'
'Codeshala'

>>> word = 'Code Shala'
>>> word
'Code Shala'
>>> word[0]
'C'
>>> word[6]
'h'
>>> word[-1]
'a'
>>> word[-5]
'S'

'In addition to indexing, slicing is also supported. While indexing is used to obtain individual characters, slicing allows you to obtain substring'
>>> word[0:3]
'Cod'
>>> word[4:7]
' Sh'
>>> word[:3]+ word[3:]
'Code Shala'

'String Methods'
'Strip: Remove white Space from Start or End'
>>> word.strip()
'Code Shala'

'Len: Get the length of string'
>>> len(word)
10

'Upper & Lower Case'
>>> word.upper()
'CODE SHALA'
>>> word.lower()
'code shala'

'Replace'
>>> word.replace('a','@')
'Code Sh@l@'

'Split'
>>> word.split(' ')
['Code', 'Shala']

'Check string for certain phrase or character'
>>> word
'Code Shala'
>>> x = 'a' in word
>>> x
True
>>> x = 'G' in word
>>> x
False
>>> x = 'G' not in word
>>> x
True

'String Concatnate'
>>> a = 'Code'
>>> b = 'Shala'
>>> c = a + b
>>> c
'CodeShala'
>>> c = a + " " + b
>>> c
'Code Shala'

'String Format'
>>> age = 35
>>> text = "My name is Rajendra and my age is " + age
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    text = "My name is Rajendra and my age is " + age
TypeError: can only concatenate str (not "int") to str

>>> text = 'My name is Rajendra and my age is ' + str(age)
>>> text
'My name is Rajendra and my age is 35'

>>> text = "My name is Rajendra and my age is {}"
>>> text.format(age)
'My name is Rajendra and my age is 35'

>>> date = 14
>>> month = 2
>>> year = 2020
>>> msg = "Birthday of Code Shala is on {}-{}-{}"
>>> msg.format(date,month, year)
'Birthday of Code Shala is on 14-2-2020'

>>> msg = "Birthday of Code Shala is on {1}-{0}-{2}"
>>> msg.format(date,month, year)
'Birthday of Code Shala is on 2-14-2020' 
