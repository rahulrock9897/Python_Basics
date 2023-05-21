import os

"""
String Literals
Let’s first differentiate between a string literal and a string value.
A string literal is what we see in the source code of a computer program, including the quotation marks.
A string value is what we see when we call the print() function and run the program.
"""
"""
Escape character	How it formats 
"\"           New line in a multi-line string
\\	                  Backslash
’	            Apostrophe or single quote
"                  	Double quote
\n	                Line break
\t	          Tab (horizontal indentation)
"""

print("hello world")

print('hello world\'s of python')  # \  is escape sequence
"""Escape Sequences :- Suppose, you want to have a string which contains a single quote ('), how will you specify 
this string? For example, the string is What's your name?. You cannot specify 'What's your name?' because Python will 
be confused as to where the string starts and ends. So, you will have to specify that this single quote does not 
indicate the end of the string. This can be done with the help of what is called an escape sequence. You specify the 
single quote as \' - notice the backslash. Now, you can specify the string as 'What\'s your name?'. """

print("hello world's of python\"s this is without r method")  # without RAW STRING

print(r"hello world's of python\"s this is r method")  # r or R indicate RAW STRING
print(R"hello world's of python\"s this is R method")  # r or R indicate RAW STRING

print(r"this is best's of best example")

"""
A raw string tells Python to ignore all formatting within a string, including escape characters.
We create a raw string by putting an r in front of the string, right before the beginning quotation mark:
"""

# we can use the \n escape character to break lines without hitting the enter or return key:
print("This string\nspans multiple\nlines.")

# We can combine escape characters, too.
# Let’s print a multi-line string and include tab spacing for an itemized list, for example:
print("1.\tShark\n2.\tShrimp\n10.\tSquid")
