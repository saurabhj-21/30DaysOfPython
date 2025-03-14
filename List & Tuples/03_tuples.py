#tuples are immutable
a=(2, 5, 6, 1, 3)
print(type(a))

b=(2)   #this is not a tuple
print(type(b))

c=(1,)   #this is a tuple
print(type(c))

d=(3, 22, True, "Rocky", "Vai")
d(0)=333      # Gives error because tuples are immutable
print(d)

