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