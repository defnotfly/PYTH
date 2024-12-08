def op (operation, x, y):
    return operation(x,y)

add = lambda x,y : x + y
subtract = lambda x,y : x-y

result1 = op(add, 5, 3)
result2 = op(subtract, 5,3)

print(result1)
print(result2)
