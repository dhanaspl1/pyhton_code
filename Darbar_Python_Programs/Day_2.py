for i in "hello":
    print(i);

def s(name="jhon"):
    return "hello {}".format(name)

print(s("james"))

# list 
print('list')
a = [2 * x for x in range(10) if x ** 2 > 3 ]
print(a)

# Set 
print('set')
b  = {2 * x for x in range(10) if x ** 2 > 3 }
print(b)

# Dict

print('disctionary - key value pair')
c = { s : len(s) for s in ["apple", "darbar"]}
print(c)