first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
# f before the opening quote puts a variable in the string. braces around the variable name/s to be inserted. f-strings: python 3.6 and later
# can use f-strings to compose complete messages using info associated with a variable
print(f"Hello, {full_name.title()}!")

# can use f-strings to compose a message and then assign that message to a variable. cleaner printing
message = f"Hello, {full_name.title()}!"
print(message)

# python 3.5 or earlier uses format() method instead. to use, list the vars wanted in the string inside the parens, referring to each var by a set of ordered braces
full_name = "{} {}".format(first_name, last_name)
print(full_name)

# can add a tab to text with \t
print("Python")
print("\tPython")

# add a newline in a string with the character combination \n
print("Languages:\nPython\nC\nJavascript")

# can combine tabs and newlines to organize output.
print("Languages:\n\tPython\n\tC\n\tJavascript")

# rstrip() method removes whitespace from the right side of a string, but only temporarily
favorite_language = 'python   '
print(favorite_language)
stripped = favorite_language.rstrip()  # store in a variable to keep the change
print(stripped)

favorite_language = 'python   '
favorite_language = favorite_language.rstrip()
print(favorite_language)

# strip from the left with lstrip() or both sides with strip()
favorite_language = '   python   '
print(favorite_language)
both_stripped = favorite_language.strip()
print(both_stripped)
print(favorite_language)
