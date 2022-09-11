bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# accessing elements in a list by telling python the position aka index of the item desired
print(bicycles[3])

# can use any string method on any element in a list
print(bicycles[0].title())
print(bicycles)

print(bicycles[-1])
print(bicycles[-2])


message = f"My first bike was a {bicycles[0].title()}."
print(message)
