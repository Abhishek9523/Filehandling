f=open('n1.txt','w')

f.write("Hello,This is Abhishek Kumar \n I am from Bhopal")
# f.writelines()
f.writable()

data=('This is python class', 'Timing is 1:30 To 2:30')
f.writelines(data)
f.close()