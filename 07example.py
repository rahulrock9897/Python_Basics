# Exеrсiѕе fоr Quоtiеntѕ

"""Write a program, quotient.py, thаt prompts the uѕеr fоr twо integers, аnd
then рrintѕ thеm оut in a sentence with an intеgеr division рrоblеm likе
The quоtiеnt оf 14 and 3 iѕ 4 with a rеmаindеr оf 2."""
"""Note: Rеviеw Diviѕiоn and Remainders if уоu fоrgеt thе intеgеr division оr remainder operator."""

# solution

one = int(input("enter first number :- "))
second = int(input("enter second number :- "))

div = int(one/second)
quotient = one // second
remainder = one % second

print("Div is :- ", div)
print("Remainder is :- ", remainder)
print("Quotient is :- ", quotient)

print("the quotient of", one, "and", second, "is", quotient, "with a remainder of", remainder, sep=" ")