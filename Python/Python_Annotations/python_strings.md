# Python - Working with methods
Python version used - 3.6.5
To test and learn with the codes above, digit line by line, don't copy and paste.
You can make a .py script or enter python3 on terminal to access python shell. 


## Slice
Return a slice object representing the set of indices specified by range(start, stop, step).
```python
var = 'slack'
>>> var[3]   # Take the third character 'C'.
>>> var[-1]  # Take the last character.
>>> var[0] + var[4]  # Concatenates s and k.
>>> var[:5]  # Select character 0 to 5 'Slack'
>>> var[1:4]  # Select character 1 to 4 'lac'
>>> var[1:4:2]  # Select caracter 1 to 4 jumping one position 'lc'.
>>> varlist = ['1','2','3','4','5']
>>> varlist[0::2]  # This can be used on lists and tuples
```
    OUT
    >>> c
    >>> k
    >>> sk
    >>> slack
    >>> lac
    >>> lc
    >>> ['1', '3', '5']

## Split() Method
    .split() - Return a list of the words in the string, using sep as the delimiter string.
```python
>>> hour = '02:56:58'
>>> hour.split(':') # returns ['02', '56', '58']
>>> hour.split(':')[1] # Returns 56
>>> h, m, s = hour.split(':') # Each variable will receive a splitted value
>>> hour.rsplit(':', 1) # Splits a value to the right
```
    OUT
    >>> ['02', '56', '58']
    >>> 56
    >>> ['02:56', '58']

## Join() Method
    .join() - Return a string which is the concatenation of the strings in iterable.
```python
>>> '-'.join(n_list) # returns 1-2-3-4-5
>>> a1 = 'abc'
>>> a2 = '123'
>>> n_list = ['1', '2', '3', '4', '5'] # Join can be used with tuples also
>>> a2.join(a1) # returns a123b123c
>>> # Usage example for index, join, split and rsplit
>>> name = str(input('Enter your full name: '))
>>> ''.join(name.split()[0] + ' ' + name.rsplit(' ', 1)[1]) ''' This line will return your name
                                                            and last name, regardless of how many are.''
```
     OUT
     >>> 1-2-3-4-5
     >>> a123b123c
     >>> Enter your full name: Diego Leão Magalhães
     >>> 'Diego Magalhães'

# String interpolation
Python 3.6 brings a new and simple form to work with strings, the Literal String Interpolation or f-strings (PEP 498).
```python
>>> name = 'Diego'
>>> pyver = 'Python 3.6'
>>> print(f'Hello {name}, i\'m {pyver}') # Returns "Hello Diego, i'm Python 3.6"
>>> a = 12
>>> b = 3
>>> #Math operators inside f-strings
>>> print(f'Sum of 12 and 3 = {a + b}.') # 15
>>> print(f'Subtracting 3 of 12 = {a - b}.') # 9
>>> print(f'multiplying 12 by 3 = {a * b}.') # 36
>>> print(f'Quotient from floor division of 12 and 3 = {a // b}.') #4
>>> print(f'Dividing 12 by 3 = {a / b}.') # 4.0
>>> print(f'Remainder of division 12 by 3 = {a % b}.') # 0
>>> print(f'A to B power = {12**3}') # 1728
```
    OUT
    >>> Hello Diego, i'm Python 3.6
    >>> Sum of 12 and 3 = 15.
    >>> Subtracting 3 of 12 = 9.
    >>> multiplying 12 by 3 = 36.
    >>> Quotient from floor division of 12 and 3 = 4.
    >>> Dividing 12 by 3 = 4.0.
    >>> Remainder of division 12 by 3 = 0.
    >>> A to B power = 1728

## upper() - lower() - capitalize() - title() - casefold()
**.upper()** - Return a copy of the string with all the cased characters converted to uppercase.<br>
**.lower()** - Return a copy of the string with all the cased characters converted to lowercase.<br>
**.capitalize()** - Return a copy of the string with its first character capitalized and the rest lowercased.<br>
**.title()** - Return a titlecased version of the string where words start with an uppercase character and the remaining characters are lowercase.<br>
**.casefold()** - Return a casefolded copy of the string. Casefolded strings may be used for caseless matching.<br>

```python
tongue_twister = 'I saw Susie sitting in a shoe shine shop. Where she sits she shines, and where she shines she sits.'
>>> print(tongue_twister.capitalize())
>>> print(tongue_twister.title())
>>> print(tongue_twister.upper())
>>> print('I SAW SUSIE SITTING IN A SHOE SHINE SHOP. WHERE SHE SITS SHE SHINES,'
          'AND WHERE SHE SHINES SHE SITS.'.lower())
>>> name = str(input('Enter your name: ')).title()
>>> print(name'\n')
>>> var = 'Borussia Dortmund Fußballverein'
>>> print('Borussia Dortmund Fußballverein is converted to\n', var.casefold())  # German 'ß' becomes 'ss'
```
    OUT
    >>> I saw susie sitting in a shoe shine shop. where she sits she shines, and where she shines she sits.
    >>> I Saw Susie Sitting In A Shoe Shine Shop. Where She Sits She Shines, And Where She Shines She Sits.
    >>> I SAW SUSIE SITTING IN A SHOE SHINE SHOP. WHERE SHE SITS SHE SHINES, AND WHERE SHE SHINES SHE SITS.
    >>> i saw susie sitting in a shoe shine shop. where she sits she shines,and where she shines she sits.
    >>> Enter your name: dIegO mAgalhãEs
    >>> Diego Magalhães

    >>> Borussia Dortmund Fußballverein is converted to
    >>> borussia dortmund fussballverein

## center() - count() - endswith() - find() - rfind

**.center()** - Return centered in a string of length width. Padding is done using the specified fillchar (default is an ASCII space).<br>
**.count()** - Return the number of non-overlapping occurrences of substring sub in the range [start, end]. Optional arguments start and end are interpreted as in slice notation.<br>
**.endswith()** - Return __True__ if the string ends with the specified suffix, otherwise return __False__.<br>
**.find()** - Return the lowest index in the string where substring sub is found within the slice s[start:end]. Optional arguments start and end are interpreted as in slice notation. Return -1 if sub is not found.<br>
**.rfind()** - Return the highest index in the string where substring sub is found, such that sub is contained within s[start:end]. Optional arguments start and end are interpreted as in slice notation. Return -1 on failure.
```python
#center() example
>>> print('i\'m on the center \o/'.center(40))
>>> var = 'How can a clam cram in a clean cream can?'
#  count() example
>>> print(f'How many times \'c\' appears on \'var\'? The answer is {var.count("c")} times') # a method inside a f-string? Cool, isn't it?
#  endswith() examples
>>> print(f'{var} ends with "can"? {var.endswith("can?")}')
>>> print(f'{var} ends with "bottle"? {var.endswith("bottle?")}')
>>> print(f'The word \'can?\' appears after index? 7? {var.title().endswith("can?", 7)}') # Returns False. But 'can?' appears in the sentence end. Try to figure what happened here.
>>> print(f'The sentence have "monkey" or "bottle" at the end? {var.endswith(("monkey", "queen"))}') #  Looks for a match using a tuple of strings.
#  find() examples
>>> print(f'The word "clean" begins on index: {var.find("clean")}') #  if .find don't find the string, the method returns -1
>>> print(f'The word "Amsterdam" in \'var\', begins on index:', var.rfind('Amsterdam'))
```
    OUT
     >>>     i'm in the center
     >>> How many times 'c' appears on 'var'? The answer is 6 times
     >>> How can a clam cram in a clean cream can? ends with "can"? True
     >>> How can a clam cram in a clean cream can? ends with "bottle"? False
     >>> The word 'can?' appears after index? 7? False
     >>> The sentence have "monkey" or "bottle" at the end? False
     >>> The word "clean" begins on index: 25
     >>> The word "Amsterdam" in 'var', begins on index: -1

## replace() - isalpha() - isalnum() - isdigit() - isdecimal()
**.replace()** - Return a copy of the string with all occurrences of substring old replaced by new.<br>
**.isalpha()** - Return true if all characters in the string are alphabetic and there is at least
one character, false otherwise.<br>
**.isalnum()** - Return true if all characters in the string are alphanumeric and there is
at least one character, false otherwise.<br>
**.isdigit()** - Return true if all characters in the string are digits and there is at least one character, false otherwise.<br>
**.isdecimal()** - Return true if all characters in the string are decimal characters and there is at least one character, false otherwise.<br>
```python
>>> itin = '927-74-7146'  # Example itin number
>>> print(f'ITIN number {itin}')
>>> varitin = ''.join(itin.replace('-', '').split('.'))
>>> print(f'With Replace, split and join, this is the result: {varitin}') # I just want the numbers
>>> print(f'O valor da linha acima é numérico? {varitin.isnumeric()}')
>>> print('The acronym ITIN is alphabetical?', 'ITIN'.isalpha())
>>> print(f'My car chassis is 9BWZZZ377VT004251, this code is alphanumeric?', '9BWZZZ377VT004251'.isalnum())
>>> print('The value "asdjh1238" is digit?', 'asdjh1238'.isdigit())
>>> print('The value "32212011" is digit?', '32212011'.isdigit())
>>> print('The value "asdjh1238" is decimal?', 'asdjh1238'.isdecimal())
>>> print('The value "32212011" is decimal?', '32212011'.isdecimal())
```
    OUT
    >>> ITIN number 927-74-7146
    >>> With Replace, split and join, this is the result: 927747146
    >>> O valor da linha acima é numérico? True
    >>> The acronym ITIN is alphabetical? True
    >>> My car chassis is 9BWZZZ377VT004251, this code is alphanum? True
    >>> The value "asdjh1238" is digit? False
    >>> The value "32212011" is digit? True
    >>> The value "asdjh1238" is decimal? False
    >>> The value "32212011" is decimal? True

References:<br>
Python Software Foundation - [Python docs - Built-in Types](https://docs.python.org/3/library/stdtypes.html)