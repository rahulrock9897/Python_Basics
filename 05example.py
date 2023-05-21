"""Prompt thе uѕеr for two numbеrѕ, аnd thеn
print out a sentence ѕtаrting thе ѕum. Fоr inѕtаnсе if thе uѕеr entered 2 and 3,
you would рrint ‘The sum of 2 аnd 3 iѕ 5."""

# without interger type 
firstnu = input("enter first number:- ")
secondnu = input("enter second number:- ")
sum = firstnu + secondnu
print("the sum of" , firstnu,"and", secondnu,"is " + sum)

# with integer type
firstno = int(input("enter your first number :- "))
secondno = int(input("enter your second number :- "))
summ = firstno + secondno
print("the sum of", firstno, "and", secondno, "is", summ, sep=" ")
