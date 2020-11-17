>>> 'welcome'
'welcome'
>>> "welcome"
'welcome'

>>> 'Welcome to Rajendra's Code Shala'
SyntaxError: invalid syntax
>>> "Welcome to Rajendra's Code Shala"
"Welcome to Rajendra's Code Shala"
>>> 'Welcome to Rajendra \n Code Shala'
'Welcome to Rajendra \n Code Shala'

>>> print('Welcome to Rajendra \n Code Shala')
Welcome to Rajendra 
 Code Shala

>>> print(r'Welcome to Rajendra \n Code Shala')
Welcome to Rajendra \n Code Shala

>>> print('C:\Users\Name')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape

>>> print(r'C:\Users\Name')
C:\Users\Name

>>> 'Code' + 'Shala'
'CodeShala'

>>> 'Code' 'Shala'
'CodeShala'

>>> fname = 'Code'
>>> fname 'Shala'
SyntaxError: invalid syntax

>>> fname + 'Shala'
'CodeShala'

>>> fname
'Code'

>>> print('Next Step--->')

>>> 'Code' 'Shala'
'CodeShala'
>>> 'Code' + 'Shala'
'CodeShala'
>>> 2 * 'Code' + 'Shala'
'CodeCodeShala'
>>> 10 * 'Code' + 'Shala'
'CodeCodeCodeCodeCodeCodeCodeCodeCodeCodeShala'
>>> 'Code' ' ' 'Shala'
'Code Shala'
>>> 'Code' '$' 'Shala'
'Code$Shala'
>>> 'Code' ' # ' 'Shala'
'Code # Shala'

>>> word = 'Code Shala'
>>> word
'Code Shala'
>>> word[3]
'e'
>>> word[9]
'a'
>>> word[8]
'l'
>>> word[-1]
'a'
>>> word[-10]
'C'
>>> word[-6]
' '
>>> word[4]
' '
>>> word
'Code Shala'

>>> word[1:3]
'od'
>>> word[7:9]
'al'
>>> word[7:10]
'ala'
>>> word[7:12]
'ala'
>>> word[:3]
'Cod'
>>> word[:]
'Code Shala'
>>> word[:4]
'Code'
>>> word[:4] + word[4:]
'Code Shala'
>>> demo = 'example1.py'
>>> demo[9:]
'py'
>>> demo[-2:-1]
'p'
>>> demo[-2:]
'py'
>>> demo = 'first.py'
>>> demo[-2:]
'py'

>>> print('Strip()')
Strip()
>>> word = ' Code Shala '
>>> word
' Code Shala '
>>> word.strip()
'Code Shala'
>>> word
' Code Shala '
>>> word.rstrip()
' Code Shala'
>>> word.lstrip()
'Code Shala '

>>> len(word)
12

>>> word.upper()
' CODE SHALA '
>>> word
' Code Shala '
>>> word.lower()
' code shala '
>>> word.replace('a','@')
' Code Sh@l@ '
>>> word
' Code Shala '
>>> word.replace('x','@')
' Code Shala '
>>> word
' Code Shala '
>>> word.split()
['Code', 'Shala']

>>> word1 = 'I Code Shala #'
>>> word1.split()
['I', 'Code', 'Shala', '#']
>>> x = 'a' in word
>>> x
True
>>> y = 'x' in word
>>> y
False
>>> _
False
>>> y = 'x' not in word
>>> y
True
>>> 
