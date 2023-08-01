#pass by value
def modify_value(x):
    x += 10

value = 5
modify_value(value)
print(value)