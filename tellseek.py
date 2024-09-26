f=open('n1.txt','rb')
print(f.tell())
print (f.read (6))
print (f.tell ())
# print (f.read (5))
print (f.seek (5,1))
print (f.tell ())
print (f.read (10))

#----------reverse---------------
# print(f.tell())
print(f.seek(-6,2))
print(f.read())

# 1 page mae likha module
# 1 copy koo package kehte hai
# copy ke under pages koo library kehte hai