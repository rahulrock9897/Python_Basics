# Sometimes we may want to construct strings from other information. This is where
# the format() method is useful.

name = "rahul"
age = 25

formatting = "{0} is {1} years old".format(name, age)

show = "why is {0} playing with python ? ".format(name)

print(formatting)
print(show)

help(abs)
# This is a wrapper around pydoc.help that provides a helpful message when
# 'help' is typed at the Python interactive prompt.
