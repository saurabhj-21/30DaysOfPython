'''Write a program to greet all the person names stored in a list ‘l’ 
and which starts with S using a while loop.'''

l = ["Partho", "Sandy", "Rohan", "sahil", "Shivam", "Amit"]
i = 0
while(i < len(l)):
    if l[i].startswith("S") or l[i].startswith("s"):
        print(f"Hello {l[i]}")
    i += 1